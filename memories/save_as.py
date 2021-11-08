from PIL import Image
import os
import numpy as np
import requests


def open_image(image_path: str) -> np.ndarray:
    """Open image as array

    Takes an image path as input and returns the image file to the user.
    Can be then used for further processing or to save in any format required.

    Args:
        image_path (str): Path to image to be saved

    Returns:
        np.ndarray: PIL formatted image as array
    """

    if image_path.startswith('http'):
        response = requests.get(image_path, stream=True)
        response.raw.decode_content = True
        image_path = response.raw

    image = Image.open(image_path).convert("RGB")
    image = np.asarray(image)

    return image


def save_image(input_image: np.ndarray or list, output_path: str) -> None:
    """Save an image or list of image in any format you want

    Implementation of PIL to save image or list of images to an output folder.
    Needs the output path with the file extension in either case and
    input_image should be np.ndarray or list of np.ndarray. When provided with
    a list of image paths, and savefolder, this will create a pdf file with all
    the images (at their full resolution).

    Args:
        input_image (np.ndarray or list): Image to be saved
        output_path (str): output file path where image is to be saved

    Todo:
        Improve readability of docstring and function documentation
        Fix documentation
    """

    file_path, file_name = os.path.split(output_path)
    os.makedirs(file_path, exist_ok=True)
    file_name, file_extension = file_name.split(".")[0], file_name.split(
        ".")[-1]

    if type(input_image) is list:
        if output_path.split(".")[-1] == 'pdf':
            updated_image_list = []
            for each_path in input_image:
                updated_image_list.append(Image.open(each_path).convert("RGB"))

            updated_image_list[0].save(output_path, "PDF",
                                       resolution=100.0, save_all=True,
                                       append_images=updated_image_list[1:])
        else:
            for count, each_image in enumerate(input_image):
                output_image_path = os.path.join(
                    file_path,
                    file_name + "-" + str(count) + "." + file_extension)
                each_image = Image.fromarray(each_image)
                each_image.save(output_image_path)
    else:
        input_image = Image.fromarray(input_image)
        input_image.save(output_path)
