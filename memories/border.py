import cv2
import os

def makeBorder(imageInputPath: str, borderType: str, bgrVal: list = [255, 255, 255], borderDimensions: list = None) -> None:
    """Add a border to the image. CUrrently in development and can only make a solid color border at 1% width/height (whichever is greater)

    :param imageInputPath: The path of the input image is to be passed
    :type imageInputPath: str
    :param borderType: Select the border type you want
    :type borderType: str
    :param bgrVal: The BGR value of the background in a list
    :type bgrVal: list, optional
    :param borderDimensions: The value (in pixels) of the border to be made, order is in top, bottom, left, right. Default value is 1% of max(imageheight, imagewidth)
    :type borderDimensions: list, optional
    """

    image = cv2.imread(imageInputPath)
    
    if borderDimensions == None:
        borderDimensions = [max(image.shape[0], image.shape[1]) // 100]*4
    
    image = cv2.copyMakeBorder(image, borderDimensions[0], borderDimensions[1], borderDimensions[2], borderDimensions[3], cv2.BORDER_CONSTANT, value=bgrVal)

    filepath, fileName = os.path.split(imageInputPath)
    fileName = fileName.split(".")
    newFileName = fileName[0] + " - border." + fileName[1]

    imagePath = os.path.join(filepath, newFileName)
    cv2.imwrite(imagePath, image)