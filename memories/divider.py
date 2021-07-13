import os
import cv2
import numpy as np
import copy

def dividedCrop(imageInputPath: str, imageFolderOutputPath: str, imageQuantity: int = 6, bgrVal: list = None) -> None:
    """Divide a single image into multiple smaller ones. Uses background color

    :param imageInputPath: The path of the input image is to be passed
    :type imageInputPath: str
    :param imageFolderOutputPath: The path of the folder where the output image(s) are to be saved
    :type imageFolderOutputPath: str
    :param imageQuantity: Number of images that are present in the pic
    :type imageQuantity: int, optional
    :param bgrVal: The HSV value of the background in a list
    :type bgrVal: list, optional
    """

    imagePath = imageInputPath
    imageQuantity = imageQuantity + 5
    image = cv2.imread(imagePath)

    h, w, channels = image.shape
    imageArea = h*w

    if bgrVal:
        bgrVal = np.uint8([[bgrVal]])
        hsvVal = list(cv2.cvtColor(bgrVal, cv2.COLOR_BGR2HSV)[0][0])
        imageRot_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        lowerThreshVals = (max(int(hsvVal[0])-5, 0), max(int(hsvVal[1])-20, 0), max(int(hsvVal[2])-25, 0))
        upperThreshVals = (min(int(hsvVal[0])+5, 180), min(int(hsvVal[1])+20, 255), min(int(hsvVal[2])+25, 255))
        
        thresh = cv2.inRange(imageRot_hsv, lowerThreshVals, upperThreshVals)
        
    else:
        imageRot_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(imageRot_grey, 205, 255, cv2.THRESH_BINARY_INV)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    i = 1
    for cnt in contours:

        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        rectArea = rect[1][0]*rect[1][1]

        if rectArea*imageQuantity > imageArea:

            # rotate the image
            picRectAngle = rect[2] + 90
            if picRectAngle>=45:
                picRectAngle = picRectAngle - 90

            rot = cv2.getRotationMatrix2D((w/2, h/2), picRectAngle, 1)
            result_img = cv2.warpAffine(copy.deepcopy(image), rot, (w, h), flags=cv2.INTER_LINEAR)

            # rotate points
            pts = np.int0(cv2.transform(np.array([box]), rot))[0]

            allXCord = [i[0] for i in pts]
            allYCord = [i[1] for i in pts]

            topLeftX, topLeftY = int(min(allXCord)), int(min(allYCord))
            bottomRightX, bottomRightY = int(max(allXCord)), int(max(allYCord))
            
            img_crop = result_img[topLeftY:bottomRightY, topLeftX:bottomRightX]

            os.makedirs(imageFolderOutputPath, exist_ok=True)
            
            fileName = os.path.split(imageInputPath)[1]
            newFileName = fileName.split(".")[0] + " - " + str(i) + ".jpg"
            newImagePath = os.path.join(imageFolderOutputPath, newFileName)
            
            cv2.imwrite(newImagePath, img_crop)

            i = i + 1