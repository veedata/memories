import os
import piexif
from datetime import datetime
import logging


def add_date(image_path: str, new_datetime: str) -> None:
    """Add date when the image was originally taken

    Args:
        image_path (str): path of image (jpg)
        new_datetime (str): Date in the format "day/month/year hours:mins:secs"
    """

    try:
        exif_dict = piexif.load(image_path)

        new_exif_date = datetime.strptime(new_datetime, '%d/%m/%Y %H:%M:%S')
        new_exif_date = new_exif_date.strftime('%Y:%m:%d %H:%M:%S')

        exif_date_today = datetime.today()
        exif_date_today = exif_date_today.strftime('%Y:%m:%d %H:%M:%S')

        exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = new_exif_date
        exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = exif_date_today

        exif_bytes = piexif.dump(exif_dict)
        piexif.insert(exif_bytes, image_path)
    except Exception as ex:
        logging.error("Exception " + str(ex) + " occurred", exc_info=True)
    except SystemExit:
        pass


def bulk_add_date(folder_path: str, new_datetime: str) -> None:
    """Add date to all images in a folder

    Args:
        folder_path (str): The path of folder
        new_datetime (str): Date in the format "day/month/year hours:mins:secs"
    """

    for (dir_path, dir_names, file_names) in os.walk(folder_path):
        for each_file in file_names:
            image_path = os.path.join(dir_path, each_file)
            add_date(image_path, new_datetime)


def add_date_png(image_path: str, new_datetime: str) -> None:
    """Add date when the image was originally taken for png images
    Under Testing and does not work currently!

    Args:
        image_path (str): path of image (png)
        new_datetime (str): Date in the format "day/month/year hours:mins:secs"
    """

    # This is in testing for now
    new_exif_date = datetime.strptime(new_datetime, '%d/%m/%Y %H:%M:%S')
    new_exif_date = new_exif_date.isoformat()

    with open(image_path, 'rb') as f:
        content = f.read()

    byte_str = bytes("eXIf...%tEXtCreateDate." + new_exif_date + "...IEND",
                     "utf-8")

    broken_png = content.split(b"IEND")
    new_png = broken_png[0] + byte_str + broken_png[1]

    with open(image_path + "-1.png", 'wb') as p:
        p.write(new_png)
