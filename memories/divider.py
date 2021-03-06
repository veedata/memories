import cv2
import numpy as np
import copy


def rotate_image(mat: np.ndarray, angle: int):
    """Rotates the image without cropping the edges

    Args:
        mat (np.ndarray): Your input Image array
        angle (int): Rotation angle

    Returns:
        np.ndarray: Rotated image as output
        np.ndarray: Rotation matrix
    """

    height, width = mat.shape[:2]
    image_center = (width / 2, height / 2)

    rotation_mat = cv2.getRotationMatrix2D(image_center, angle, 1)

    abs_cos = abs(rotation_mat[0, 0])
    abs_sin = abs(rotation_mat[0, 1])

    bound_w = int(height * abs_sin + width * abs_cos)
    bound_h = int(height * abs_cos + width * abs_sin)

    rotation_mat[0, 2] += bound_w / 2 - image_center[0]
    rotation_mat[1, 2] += bound_h / 2 - image_center[1]

    rotated_mat = cv2.warpAffine(mat,
                                 rotation_mat, (bound_w, bound_h),
                                 flags=cv2.INTER_LINEAR)

    return rotated_mat, rotation_mat


def divided_crop(image: np.ndarray,
                 image_quantity: int,
                 bgr_value: list = [255, 255, 255]) -> list:
    """Divide a single image into multiple smaller ones.

    Convert a cluster of images into individual images based on background
    color to find divisions. Image quantity is used in order to get a better
    accuracy and reduce noise in the process.

    Args:
        image (np.ndarray): The path of the input image is to be passed
        image_quantity (int, optional): Number of images that are present
         in the pic.
        bgr_value (list, optional): The approx BGR value of the background
         in a list. Defaults to [255, 255, 255].

    Returns:
        list: np.ndarray list containing all cropped out images
    """

    border_dim = max(image.shape[0], image.shape[1]) // 100

    image = cv2.copyMakeBorder(image,
                               border_dim,
                               border_dim,
                               border_dim,
                               border_dim,
                               cv2.BORDER_CONSTANT,
                               value=bgr_value)
    bgr_value = np.uint8([[bgr_value]])

    hsv_value = list(cv2.cvtColor(bgr_value, cv2.COLOR_BGR2HSV)[0][0])
    image_rot_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_thresh = (max(int(hsv_value[0]) - 5, 0),
                    max(int(hsv_value[1]) - 20, 0),
                    max(int(hsv_value[2]) - 25, 0))
    upper_thresh = (min(int(hsv_value[0]) + 5, 180),
                    min(int(hsv_value[1]) + 20, 255),
                    min(int(hsv_value[2]) + 25, 255))

    thresh = cv2.inRange(image_rot_hsv, lower_thresh, upper_thresh)
    thresh = cv2.bitwise_not(thresh)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    divided_images = []
    for image_number in range(0, image_quantity):

        rect = cv2.minAreaRect(contours[image_number])
        box = cv2.boxPoints(rect)
        box = np.int0(box)

        # rotate the image
        image_rect_area = rect[2]
        if rect[2] >= 45:
            image_rect_area = image_rect_area - 90

        result_img, rot = rotate_image(copy.deepcopy(image), image_rect_area)

        # rotate points
        pts = np.int0(cv2.transform(np.array([box]), rot))[0]

        all_x_coords = [i[0] for i in pts]
        all_y_coords = [i[1] for i in pts]

        top_left_x, top_left_y = int(min(all_x_coords)), int(min(all_y_coords))
        bottom_right_x, bottom_right_y = int(max(all_x_coords)), int(
            max(all_y_coords))

        img_crop = result_img[top_left_y:bottom_right_y,
                              top_left_x:bottom_right_x].copy()
        divided_images.append(img_crop)

    return divided_images
