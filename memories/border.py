import cv2
import numpy as np


def make_border(input_image: np.ndarray,
                border_type: str = "normal",
                bgr_value: list = [255, 255, 255, 255],
                border_dimension: list = None,
                radius_dimension: list = None) -> None:
    """Add a border to the image.

    Function to add a straight or curved edge border to the image. The borders
    can be individually sized, width for straight border type, and width +
    radius curvature, both for curved border. This will make the border a part
    of the image.

    Args:
        input_image (np.ndarray): The path of the input image is to be passed
        border_type (str, optional): Select border type - normal, curved.
         Defaults to "normal".
        bgr_value (list, optional): The BGRA value of the background in a list
         ([B, G, R, A]). Defaults to [255, 255, 255, 255].
        border_dimension (list, optional): The value (in pixels) of border.
         Order is top, bottom, left, right. Defaults to 1% of max(ht, wt).
        radius_dimension (list, optional): The value (in pixels) of the corner
         radius, order is in top-right, top-left, bottom-right, bottom-left.

    Todo:
        Other types of border colors - gradiants and multicolor options
    """

    image = input_image

    if border_dimension is None:
        border_dimension = [max(image.shape[0], image.shape[1]) // 100] * 4
    elif type(border_dimension) is int:
        border_dimension = [border_dimension] * 4

    if radius_dimension is None:
        radius_dimension = [max(image.shape[0], image.shape[1]) // 100] * 4
    elif type(radius_dimension) is int:
        radius_dimension = [radius_dimension] * 4

    if border_type == "normal":
        image = cv2.copyMakeBorder(image,
                                   border_dimension[0],
                                   border_dimension[1],
                                   border_dimension[2],
                                   border_dimension[3],
                                   cv2.BORDER_CONSTANT,
                                   value=bgr_value)

    elif border_type == "curved":
        image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
        image = cv2.copyMakeBorder(image,
                                   border_dimension[0],
                                   border_dimension[1],
                                   border_dimension[2],
                                   border_dimension[3],
                                   cv2.BORDER_CONSTANT,
                                   value=(255, 255, 255, 0))

        top_left = (0, 0)
        top_right = (image.shape[1], 0)
        bottom_right = (image.shape[1], image.shape[0])
        bottom_left = (0, image.shape[0])

        # straight lines
        cv2.line(
            image,
            (top_left[0] + radius_dimension[0] + border_dimension[0] // 2,
             top_left[1] + border_dimension[0] // 2),
            (top_right[0] - radius_dimension[1] - border_dimension[0] // 2,
             top_right[1] + border_dimension[0] // 2), bgr_value,
            abs(border_dimension[0]), cv2.LINE_AA)
        cv2.line(image,
                 (top_right[0] - border_dimension[0] // 2, top_right[1] +
                  radius_dimension[1] + border_dimension[0] // 2),
                 (bottom_right[0] - border_dimension[0] // 2, bottom_right[1] -
                  radius_dimension[2] - border_dimension[0] // 2), bgr_value,
                 abs(border_dimension[0]), cv2.LINE_AA)
        cv2.line(
            image,
            (bottom_right[0] - radius_dimension[2] - border_dimension[0] // 2,
             bottom_left[1] - border_dimension[0] // 2),
            (bottom_left[0] + radius_dimension[3] + border_dimension[0] // 2,
             bottom_right[1] - border_dimension[0] // 2), bgr_value,
            abs(border_dimension[0]), cv2.LINE_AA)
        cv2.line(image,
                 (bottom_left[0] + border_dimension[0] // 2, bottom_left[1] -
                  radius_dimension[3] - border_dimension[0] // 2),
                 (top_left[0] + border_dimension[0] // 2, top_left[1] +
                  radius_dimension[0] + border_dimension[0] // 2), bgr_value,
                 abs(border_dimension[0]), cv2.LINE_AA)

        # arcs
        cv2.ellipse(
            image,
            (top_left[0] + radius_dimension[0] + border_dimension[0] // 2,
             top_left[1] + radius_dimension[0] + border_dimension[0] // 2),
            (radius_dimension[0], radius_dimension[0]), 180, 0, 90, bgr_value,
            border_dimension[0], cv2.LINE_AA)
        cv2.ellipse(
            image,
            (top_right[0] - radius_dimension[1] - border_dimension[0] // 2,
             top_right[1] + radius_dimension[1] + border_dimension[0] // 2),
            (radius_dimension[1], radius_dimension[1]), 270, 0, 90, bgr_value,
            border_dimension[0], cv2.LINE_AA)
        cv2.ellipse(
            image,
            (bottom_right[0] - radius_dimension[2] - border_dimension[0] // 2,
             bottom_right[1] - radius_dimension[2] - border_dimension[0] // 2),
            (radius_dimension[2], radius_dimension[2]), 0, 0, 90, bgr_value,
            border_dimension[0], cv2.LINE_AA)
        cv2.ellipse(
            image,
            (bottom_left[0] + radius_dimension[3] + border_dimension[0] // 2,
             bottom_left[1] - radius_dimension[3] - border_dimension[0] // 2),
            (radius_dimension[3], radius_dimension[3]), 90, 0, 90, bgr_value,
            border_dimension[0], cv2.LINE_AA)

    return image
