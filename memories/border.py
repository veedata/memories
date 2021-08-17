import cv2
import os

def makeBorder(imageInputPath: str, borderType: str = "normal", bgrVal: list = [255, 255, 255, 255], borderDimensions: list = None, radiusDimensions: list = None) -> None:
    """Add a border to the image. CUrrently in development and can only make a solid color border at 1% width/height (whichever is greater)

    :param imageInputPath: The path of the input image is to be passed
    :type imageInputPath: str
    :param borderType: Select the border type you want - normal, curved (default is normal)
    :type borderType: str
    :param bgrVal: The BGR value of the background in a list
    :type bgrVal: list, optional
    :param borderDimensions: The value (in pixels) of the border to be made, order is in top, bottom, left, right. Default value is 1% of max(imageheight, imagewidth)
    :type borderDimensions: list, optional
    :param radiusDimensions: The value (in pixels) of the curvature of radius to be made, order is in top-right, top-left, bottom-right, bottom-left.
    :type radiusDimensions: list, optional
    """

    image = cv2.imread(imageInputPath)
    
    if borderDimensions is None:
        borderDimensions = [max(image.shape[0], image.shape[1]) // 100]*4
    
    if borderType == "normal":        
        image = cv2.copyMakeBorder(image, borderDimensions[0], borderDimensions[1], borderDimensions[2], borderDimensions[3], cv2.BORDER_CONSTANT, value=bgrVal)

    elif borderType == "curved":
        image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
        image = cv2.copyMakeBorder(image, borderDimensions[0], borderDimensions[1], borderDimensions[2], borderDimensions[3], cv2.BORDER_CONSTANT, value=(255, 255, 255, 0))

        if len(bgrVal) <= 3:
            bgrVal.append(255)
        else:
            bgrVal[3] = 255

        bottom_right = (image.shape[0], image.shape[1])

        top_left = (0, 0)
        top_right = (bottom_right[1], top_left[1])
        bottom_left = (top_left[0], bottom_right[0])
        bottom_right = (bottom_right[1], bottom_right[0])

        # straight lines
        cv2.line(image, (top_left[0] + radiusDimensions[0] + borderDimensions[0]//2, top_left[1] + borderDimensions[0]//2), (top_right[0] - radiusDimensions[1] - borderDimensions[0]//2, top_right[1] + borderDimensions[0]//2), bgrVal, abs(borderDimensions[0]), cv2.LINE_AA)
        cv2.line(image, (top_right[0] - borderDimensions[0]//2, top_right[1] + radiusDimensions[1] + borderDimensions[0]//2), (bottom_right[0] - borderDimensions[0]//2, bottom_right[1] - radiusDimensions[2] - borderDimensions[0]//2), bgrVal, abs(borderDimensions[0]), cv2.LINE_AA)
        cv2.line(image, (bottom_right[0] - radiusDimensions[2] - borderDimensions[0]//2, bottom_left[1] - borderDimensions[0]//2), (bottom_left[0] + radiusDimensions[3] + borderDimensions[0]//2, bottom_right[1] - borderDimensions[0]//2), bgrVal, abs(borderDimensions[0]), cv2.LINE_AA)
        cv2.line(image, (bottom_left[0] + borderDimensions[0]//2, bottom_left[1] - radiusDimensions[3] - borderDimensions[0]//2), (top_left[0] + borderDimensions[0]//2, top_left[1] + radiusDimensions[0] + borderDimensions[0]//2), bgrVal, abs(borderDimensions[0]), cv2.LINE_AA)

        # arcs
        cv2.ellipse(image, (top_left[0] + radiusDimensions[0] + borderDimensions[0]//2, top_left[1] + radiusDimensions[0] + borderDimensions[0]//2), (radiusDimensions[0], radiusDimensions[0]), 180, 0, 90, bgrVal, borderDimensions[0], cv2.LINE_AA)
        cv2.ellipse(image, (top_right[0] - radiusDimensions[1] - borderDimensions[0]//2, top_right[1] + radiusDimensions[1] + borderDimensions[0]//2), (radiusDimensions[1], radiusDimensions[1]), 270, 0, 90, bgrVal, borderDimensions[0], cv2.LINE_AA)
        cv2.ellipse(image, (bottom_right[0] - radiusDimensions[2] - borderDimensions[0]//2, bottom_right[1] - radiusDimensions[2] - borderDimensions[0]//2), (radiusDimensions[2], radiusDimensions[2]), 0, 0, 90, bgrVal, borderDimensions[0], cv2.LINE_AA)
        cv2.ellipse(image, (bottom_left[0] + radiusDimensions[3] + borderDimensions[0]//2, bottom_left[1] - radiusDimensions[3] - borderDimensions[0]//2), (radiusDimensions[3], radiusDimensions[3]), 90, 0, 90, bgrVal, borderDimensions[0], cv2.LINE_AA)


    filepath, fileName = os.path.split(imageInputPath)
    fileName = fileName.split(".")
    if borderType == "curved":
        fileName[-1] = 'png'
    newFileName = fileName[0] + " - border." + fileName[-1]

    imagePath = os.path.join(filepath, newFileName)
    cv2.imwrite(imagePath, image)

