import cv2
import copy
import numpy as np


def make_border(inputImage: np.ndarray,
               borderType: str = "normal",
               bgrVal: list = [255, 255, 255, 255],
               borderDimensions: list = None,
               radiusDimensions: list = None) -> None:
    """Add a border to the image.
    Currently in development and can only make a solid color borders.

    :param inputImage: The path of the input image is to be passed
    :type inputImage: np.ndarray
    :param borderType: Select the border type you want - normal, curved (default is normal)
    :type borderType: str
    :param bgrVal: The BGR value of the background in a list
    :type bgrVal: list, optional
    :param borderDimensions: The value (in pixels) of the border to be made, order is in top, bottom, left, right. Default value is 1% of max(imageheight, imagewidth)
    :type borderDimensions: list, optional
    :param radiusDimensions: The value (in pixels) of the curvature of radius to be made, order is in top-right, top-left, bottom-right, bottom-left.
    :type radiusDimensions: list, optional
    """

    image = inputImage

    if borderDimensions is None:
        borderDimensions = [max(image.shape[0], image.shape[1]) // 100] * 4

    if borderType == "normal":
        image = cv2.copyMakeBorder(image,
                                   borderDimensions[0],
                                   borderDimensions[1],
                                   borderDimensions[2],
                                   borderDimensions[3],
                                   cv2.BORDER_CONSTANT,
                                   value=bgrVal)

    elif borderType == "curved":
        image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
        image = cv2.copyMakeBorder(image,
                                   borderDimensions[0],
                                   borderDimensions[1],
                                   borderDimensions[2],
                                   borderDimensions[3],
                                   cv2.BORDER_CONSTANT,
                                   value=(255, 255, 255, 0))

        # Need to add error checking conditions!
        bgrVal_opaque = copy.deepcopy(bgrVal)
        if len(bgrVal) == 3:
            bgrVal_opaque.append(255)

        top_left = (0, 0)
        top_right = (image.shape[1], 0)
        bottom_right = (image.shape[1], image.shape[0])
        bottom_left = (0, image.shape[0])

        # straight lines
        cv2.line(
            image,
            (top_left[0] + radiusDimensions[0] + borderDimensions[0] // 2,
             top_left[1] + borderDimensions[0] // 2),
            (top_right[0] - radiusDimensions[1] - borderDimensions[0] // 2,
             top_right[1] + borderDimensions[0] // 2), bgrVal_opaque,
            abs(borderDimensions[0]), cv2.LINE_AA)
        cv2.line(
            image,
            (top_right[0] - borderDimensions[0] // 2,
             top_right[1] + radiusDimensions[1] + borderDimensions[0] // 2),
            (bottom_right[0] - borderDimensions[0] // 2,
             bottom_right[1] - radiusDimensions[2] - borderDimensions[0] // 2),
            bgrVal_opaque, abs(borderDimensions[0]), cv2.LINE_AA)
        cv2.line(
            image,
            (bottom_right[0] - radiusDimensions[2] - borderDimensions[0] // 2,
             bottom_left[1] - borderDimensions[0] // 2),
            (bottom_left[0] + radiusDimensions[3] + borderDimensions[0] // 2,
             bottom_right[1] - borderDimensions[0] // 2), bgrVal_opaque,
            abs(borderDimensions[0]), cv2.LINE_AA)
        cv2.line(
            image,
            (bottom_left[0] + borderDimensions[0] // 2,
             bottom_left[1] - radiusDimensions[3] - borderDimensions[0] // 2),
            (top_left[0] + borderDimensions[0] // 2,
             top_left[1] + radiusDimensions[0] + borderDimensions[0] // 2),
            bgrVal_opaque, abs(borderDimensions[0]), cv2.LINE_AA)

        # arcs
        cv2.ellipse(
            image,
            (top_left[0] + radiusDimensions[0] + borderDimensions[0] // 2,
             top_left[1] + radiusDimensions[0] + borderDimensions[0] // 2),
            (radiusDimensions[0], radiusDimensions[0]), 180, 0, 90,
            bgrVal_opaque, borderDimensions[0], cv2.LINE_AA)
        cv2.ellipse(
            image,
            (top_right[0] - radiusDimensions[1] - borderDimensions[0] // 2,
             top_right[1] + radiusDimensions[1] + borderDimensions[0] // 2),
            (radiusDimensions[1], radiusDimensions[1]), 270, 0, 90,
            bgrVal_opaque, borderDimensions[0], cv2.LINE_AA)
        cv2.ellipse(
            image,
            (bottom_right[0] - radiusDimensions[2] - borderDimensions[0] // 2,
             bottom_right[1] - radiusDimensions[2] - borderDimensions[0] // 2),
            (radiusDimensions[2], radiusDimensions[2]), 0, 0, 90,
            bgrVal_opaque, borderDimensions[0], cv2.LINE_AA)
        cv2.ellipse(
            image,
            (bottom_left[0] + radiusDimensions[3] + borderDimensions[0] // 2,
             bottom_left[1] - radiusDimensions[3] - borderDimensions[0] // 2),
            (radiusDimensions[3], radiusDimensions[3]), 90, 0, 90,
            bgrVal_opaque, borderDimensions[0], cv2.LINE_AA)

    return image
