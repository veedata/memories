from PIL import Image
import os
import numpy as np


def openImage(inputImagepath: str) -> np.ndarray:
    """Takes an image path as input and returns the image file to the user.
    Can be then used for further processing or to save in any format required.

    :param inputImagepath: Path to image to be saved
    :type inputImagepath: str
    """

    image = Image.open(inputImagepath).convert("RGB")
    image = np.asarray(image)

    return image


def saveAsPDF(imageList: list, outputPath: str) -> None:
    """Save a list of images in PDF format

    :param imageList: List of path to all images to be saved
    :type imageList: list
    :param outputPath: The path (including file name) where PDF is to be saved
    :type outputPath: str
    """

    openImgList = []
    for eachPath in imageList:
        openImgList.append(Image.open(eachPath).convert("RGB"))

    openImgList[0].save(outputPath,
                        "PDF",
                        resolution=100.0,
                        save_all=True,
                        append_images=openImgList[1:])


def saveAs(inputImage: np.ndarray, outputPath: str) -> None:
    """Save an image or list of image in any format you want

    :param inputImage: Image to be saved
    :type inputImage: str or list
    :param outputPath: The output file path in which the image is to be saved
    :type outputPath: str
    """

    filePath, fileName = os.path.split(outputPath)
    fileName, fileExt = fileName.split(".")[0], fileName.split(".")[-1]

    if type(inputImage) is list:
        for count, eachImage in enumerate(inputImage):
            outputImagePath = os.path.join(
                filePath, fileName + "-" + str(count) + "." + fileExt)
            eachImage = Image.fromarray(eachImage)
            eachImage.save(outputImagePath)
    else:
        inputImage = Image.fromarray(inputImage)
        inputImage.save(outputPath)
