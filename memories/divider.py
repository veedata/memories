import os
import cv2
import numpy as np
import copy


def divided_crop(inputImage: np.ndarray,
                imageQuantity: int = 4,
                bgrVal: list = [255, 255, 255]) -> None:
    """Divide a single image into multiple smaller ones. Uses background color

    :param inputImage: The path of the input image is to be passed
    :type inputImage: str
    :param imageQuantity: Number of images that are present in the pic
    :type imageQuantity: int, optional
    :param bgrVal: The BGR value of the background in a list
    :type bgrVal: list, optional
    """

    image = inputImage

    h, w, channels = image.shape
    imageArea = h * w
    borderDim = max(image.shape[0], image.shape[1]) // 100

    if bgrVal != [255, 255, 255]:
        image = cv2.copyMakeBorder(image,
                                   borderDim,
                                   borderDim,
                                   borderDim,
                                   borderDim,
                                   cv2.BORDER_CONSTANT,
                                   value=bgrVal)
        bgrVal = np.uint8([[bgrVal]])

        hsvVal = list(cv2.cvtColor(bgrVal, cv2.COLOR_BGR2HSV)[0][0])
        imageRot_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        lowerThreshVals = (max(int(hsvVal[0]) - 5,
                               0), max(int(hsvVal[1]) - 20,
                                       0), max(int(hsvVal[2]) - 25, 0))
        upperThreshVals = (min(int(hsvVal[0]) + 5,
                               180), min(int(hsvVal[1]) + 20,
                                         255), min(int(hsvVal[2]) + 25, 255))

        thresh = cv2.inRange(imageRot_hsv, lowerThreshVals, upperThreshVals)

    else:
        # Soon to be retired part.. will be merged with above when smaller optimisations are made to the above code
        image = cv2.copyMakeBorder(image,
                                   borderDim,
                                   borderDim,
                                   borderDim,
                                   borderDim,
                                   cv2.BORDER_CONSTANT,
                                   value=bgrVal)

        imageRot_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(imageRot_grey, 205, 255,
                                    cv2.THRESH_BINARY_INV)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)

    dividedImages = []
    for cnt in contours:

        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        rectArea = rect[1][0] * rect[1][1]

        if rectArea * imageQuantity > imageArea:

            # rotate the image
            picRectAngle = rect[2] + 90
            if picRectAngle >= 45:
                picRectAngle = picRectAngle - 90

            rot = cv2.getRotationMatrix2D((w / 2, h / 2), picRectAngle, 1)
            result_img = cv2.warpAffine(copy.deepcopy(image),
                                        rot, (w, h),
                                        flags=cv2.INTER_LINEAR)

            # rotate points
            pts = np.int0(cv2.transform(np.array([box]), rot))[0]

            allXCord = [i[0] for i in pts]
            allYCord = [i[1] for i in pts]

            topLeftX, topLeftY = int(min(allXCord)), int(min(allYCord))
            bottomRightX, bottomRightY = int(max(allXCord)), int(max(allYCord))

            img_crop = result_img[topLeftY:bottomRightY, topLeftX:bottomRightX]
            dividedImages.append(img_crop)

    return dividedImages
