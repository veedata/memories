import PIL
import os

def saveAsPDF(imageList: list, outputFilePath: str) -> None:
    """Save a list of images in PDF format

    @type imageList: list
    @param imageList: List of path to all images to be saved
    @type outputFilePath: str
    @param outputFilePath: The path (including file name) where the output PDF is to be saved
    """
    
    openImgList = []
    for eachPath in imageList:
        openImgList.append(PIL.Image.open(eachPath).convert("RGB"))
    
    openImgList[0].save(outputFilePath, "PDF", resolution=100.0, save_all=True, append_images=openImgList)

def saveAsPNG(inputImagepath: str, outputImagePath: str) -> None:
    """Save an image as a png file

    @type inputImagepath: str
    @param inputImagepath: Path to image to be saved
    @type outputImagePath: str
    @param outputImagePath: The path where the output file is to be saved
    """
    
    imageName = os.path.split(inputImagepath)[1]
    imageName = imageName.split(".")[0] + ".png"
    outputImagePath = os.path.join(outputImagePath, imageName)

    image = PIL.Image.open(inputImagepath).convert("RGB")
    image.save(outputImagePath)

def saveAsJPG(inputImagepath: str, outputImagePath: str) -> None:
    """Save an image as a jpg file

    @type inputImagepath: str
    @param inputImagepath: Path to image to be saved
    @type outputImagePath: str
    @param outputImagePath: The path where the output file is to be saved
    """
    
    imageName = os.path.split(inputImagepath)[1]
    imageName = imageName.split(".")[0] + ".jpg"
    outputImagePath = os.path.join(outputImagePath, os.path.split(inputImagepath)[1])

    image = PIL.Image.open(inputImagepath).convert("RGB")
    image.save(outputImagePath)