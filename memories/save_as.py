from PIL import Image
import os
import numpy as np


def open_image_file(image_path: str) -> np.ndarray:
    """Takes an image path as input and returns the image file to the user.
    Can be then used for further processing or to save in any format required.

    :param image_path: Path to image to be saved
    :type image_path: str
    """

    image = Image.open(image_path).convert("RGB")
    image = np.asarray(image)

    return image


def save_pdf(image_list: list, output_path: str) -> None:
    """Save a list of images in PDF format

    :param image_list: List of path to all images to be saved
    :type image_list: list
    :param output_path: The path (including file name) where PDF is to be saved
    :type output_path: str
    """

    updated_image_list = []
    for eachPath in image_list:
        updated_image_list.append(Image.open(eachPath).convert("RGB"))

    updated_image_list[0].save(output_path,
                               "PDF",
                               resolution=100.0,
                               save_all=True,
                               append_images=updated_image_list[1:])


def save_image(input_image: np.ndarray, output_path: str) -> None:
    """Save an image or list of image in any format you want

    :param input_image: Image to be saved
    :type input_image: str or list
    :param output_path: The output file path in which the image is to be saved
    :type output_path: str
    """

    file_path, file_name = os.path.split(output_path)
    file_name, file_extension = file_name.split(".")[0], file_name.split(
        ".")[-1]

    if type(input_image) is list:
        for count, eachImage in enumerate(input_image):
            outputImagePath = os.path.join(
                file_path, file_name + "-" + str(count) + "." + file_extension)
            eachImage = Image.fromarray(eachImage)
            eachImage.save(outputImagePath)
    else:
        input_image = Image.fromarray(input_image)
        input_image.save(output_path)
