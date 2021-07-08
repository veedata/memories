from PIL import Image
import os

def openImage(inputImagepath):
    """Takes an image path as input and returns the file name of the image and opened image to the user. Can be then used fo rfurther processing or to save in any format required. 
    
    :param inputImagepath: Path to image to be saved
    :type inputImagepath: str
    """
    imageName = os.path.split(inputImagepath)[1]
    image = Image.open(inputImagepath).convert("RGB")
    imageName = imageName.split(".")[0]
    return image, imageName

def saveAsPDF(imageList: list, outputFilePath: str) -> None:
    """Save a list of images in PDF format

    :param imageList: List of path to all images to be saved
    :type imageList: list
    :param outputFilePath: The path (including file name) where the output PDF is to be saved
    :type outputFilePath: str
    """
    
    openImgList = []
    for eachPath in imageList:
        openImgList.append(Image.open(eachPath).convert("RGB"))
    
    openImgList[0].save(outputFilePath, "PDF", resolution=100.0, save_all=True, append_images=openImgList[1:])

def saveAsPNG(inputImagepath: str, outputImagePath: str) -> None:
    """Save an image as a png file

    :param inputImagepath: Path to image to be saved
    :type inputImagepath: str
    :param outputImagePath: The path where the output file is to be saved
    :type outputImagePath: str
    """
    
    image, imageName = openImage(inputImagepath)

    outputImagePath = os.path.join(outputImagePath, imageName + ".png")
    image.save(outputImagePath)

def saveAsJPG(inputImagepath: str, outputImagePath: str) -> None:
    """Save an image as a jpg file

    :param inputImagepath: Path to image to be saved
    :type inputImagepath: str
    :param outputImagePath: The path where the output file is to be saved
    :type outputImagePath: str
    """
    
    image, imageName = openImage(inputImagepath)

    outputImagePath = os.path.join(outputImagePath, imageName + ".jpg")
    image.save(outputImagePath)