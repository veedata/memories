import os
import piexif
from datetime import datetime
import logging

def addDate(imageInputPath: str, newDateTime: str) -> None:
    """Add date when the image was originally taken

    :param imageInputPath: The path of the input image is to be passed
    :type imageInputPath: str
    :param newDateTime: Date in the format "day/month/year hours:mins:secs"
    :type newDateTime: str
    """

    try:
        exif_dict = piexif.load(imageInputPath)
        
        newExifDate = datetime.strptime(newDateTime, '%d/%m/%Y %H:%M:%S')
        newExifDate = newExifDate.strftime('%Y:%m:%d %H:%M:%S')
        
        exifDateToday = datetime.today()
        exifDateToday = exifDateToday.strftime('%Y:%m:%d %H:%M:%S')

        exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = newExifDate
        exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = exifDateToday
        
        exif_bytes = piexif.dump(exif_dict)
        piexif.insert(exif_bytes, imageInputPath)
    except Exception as ex:
        logging.error("Exception " + str(ex) + " occurred", exc_info=True)
    except SystemExit:
        pass

def bulkAddDate(folderPath: str, newDateTime: str) -> None:
    """Add date to all images in a folder

    :param folderPath: The path of folder
    :type folderPath: str
    :param newDateTime: Date in the format "day/month/year hours:mins:secs"
    :type newDateTime: str
    """

    for (dirpath, dirnames, filenames) in os.walk(folderPath):
        for eachFile in filenames:
            imagePath = os.path.join(dirpath, eachFile)
            addDate(imagePath, newDateTime)

def addDatePNG(imageInputPath: str, newDateTime: str) -> None:
    """Add date when the image was originally taken for png images

    :param imageInputPath: The path of the input image is to be passed
    :type imageInputPath: str
    :param newDateTime: Date in the format "day/month/year hours:mins:secs"
    :type newDateTime: str
    """

    # This is in testing for now
    newExifDate = datetime.strptime(newDateTime, '%d/%m/%Y %H:%M:%S')
    newExifDate = newExifDate.isoformat()
    
    with open(imageInputPath, 'rb') as f:
        content = f.read()

    byteStr = bytes("eXIf...%tEXtCreateDate." + newExifDate + "...IEND", "utf-8")

    brokenPNG = content.split(b"IEND")
    newPNG = brokenPNG[0] + byteStr + brokenPNG[1]

    with open(imageInputPath+"-1.png", 'wb') as p:
        p.write(newPNG)