import cv2
import copy
import numpy as np


def make_border(input_image: np.ndarray,
                border_type: str = "normal",
                bgr_value: list = [255, 255, 255, 255],
                border_dimension: list = None,
                radius_dimension: list = None) -> None:
    """Add a border to the image.
    Currently in development and can only make a solid color borders.

    :param input_image: The path of the input image is to be passed
    :type input_image: np.ndarray
    :param border_type: Select border type - normal, curved (default is normal)
    :type border_type: str
    :param bgr_value: The BGR value of the background in a list
    :type bgr_value: list, optional
    :param border_dimension: The value (in pixels) of the border to be made,
     order is top, bottom, left, right. Default is 1% of max(height, width)
    :type border_dimension: list, optional
    :param radius_dimension: The value (in pixels) of the curvature of radius,
     order is in top-right, top-left, bottom-right, bottom-left.
    :type radius_dimension: list, optional
    """

    image = input_image

    if border_dimension is None:
        border_dimension = [max(image.shape[0], image.shape[1]) // 100] * 4

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

        # Need to add error checking conditions!
        bgr_value_opaque = copy.deepcopy(bgr_value)
        if len(bgr_value) == 3:
            bgr_value_opaque.append(255)

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
             top_right[1] + border_dimension[0] // 2), bgr_value_opaque,
            abs(border_dimension[0]), cv2.LINE_AA)
        cv2.line(image,
                 (top_right[0] - border_dimension[0] // 2, top_right[1] +
                  radius_dimension[1] + border_dimension[0] // 2),
                 (bottom_right[0] - border_dimension[0] // 2, bottom_right[1] -
                  radius_dimension[2] - border_dimension[0] // 2),
                 bgr_value_opaque, abs(border_dimension[0]), cv2.LINE_AA)
        cv2.line(
            image,
            (bottom_right[0] - radius_dimension[2] - border_dimension[0] // 2,
             bottom_left[1] - border_dimension[0] // 2),
            (bottom_left[0] + radius_dimension[3] + border_dimension[0] // 2,
             bottom_right[1] - border_dimension[0] // 2), bgr_value_opaque,
            abs(border_dimension[0]), cv2.LINE_AA)
        cv2.line(image,
                 (bottom_left[0] + border_dimension[0] // 2, bottom_left[1] -
                  radius_dimension[3] - border_dimension[0] // 2),
                 (top_left[0] + border_dimension[0] // 2, top_left[1] +
                  radius_dimension[0] + border_dimension[0] // 2),
                 bgr_value_opaque, abs(border_dimension[0]), cv2.LINE_AA)

        # arcs
        cv2.ellipse(
            image,
            (top_left[0] + radius_dimension[0] + border_dimension[0] // 2,
             top_left[1] + radius_dimension[0] + border_dimension[0] // 2),
            (radius_dimension[0], radius_dimension[0]), 180, 0, 90,
            bgr_value_opaque, border_dimension[0], cv2.LINE_AA)
        cv2.ellipse(
            image,
            (top_right[0] - radius_dimension[1] - border_dimension[0] // 2,
             top_right[1] + radius_dimension[1] + border_dimension[0] // 2),
            (radius_dimension[1], radius_dimension[1]), 270, 0, 90,
            bgr_value_opaque, border_dimension[0], cv2.LINE_AA)
        cv2.ellipse(
            image,
            (bottom_right[0] - radius_dimension[2] - border_dimension[0] // 2,
             bottom_right[1] - radius_dimension[2] - border_dimension[0] // 2),
            (radius_dimension[2], radius_dimension[2]), 0, 0, 90,
            bgr_value_opaque, border_dimension[0], cv2.LINE_AA)
        cv2.ellipse(
            image,
            (bottom_left[0] + radius_dimension[3] + border_dimension[0] // 2,
             bottom_left[1] - radius_dimension[3] - border_dimension[0] // 2),
            (radius_dimension[3], radius_dimension[3]), 90, 0, 90,
            bgr_value_opaque, border_dimension[0], cv2.LINE_AA)

    return image
