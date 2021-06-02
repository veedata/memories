import os
import piexif
from datetime import datetime
import logging

def addDate(imageInputPath: str, newDateTime: str) -> None:
    """Add date when the image was originally taken

    @type imageInputPath: str
    @param imageInputPath: The path of the input image is to be passed
    @type newDateTime: str
    @param newDateTime: Date in the format "day/month/year hours:mins:secs"
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
    except BaseException:
        pass

def bulkAddDate(folderPath: str, newDateTime: str) -> None:
    """Add date to all images in a folder

    @type folderPath: str
    @param folderPath: The path of folder
    @type newDateTime: str
    @param newDateTime: Date in the format "day/month/year hours:mins:secs"
    """

    for (dirpath, dirnames, filenames) in os.walk(folderPath):
        for eachFile in filenames:
            imagePath = os.path.join(dirpath, eachFile)
            addDate(imagePath, newDateTime)