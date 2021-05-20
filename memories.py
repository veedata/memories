import os
import cv2
import numpy as np
import math
import copy
import piexif
from datetime import datetime

def dividedCrop(imageInputPath, imageFolderOutputPath):

    imagePath = imageInputPath
    image = cv2.imread(imagePath)

    h, w, channels = image.shape
    imageArea = h*w

    imageRot_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imageRot_grey, 205, 255, cv2.THRESH_BINARY_INV)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    i = 1
    for cnt in contours:
        contourArea = cv2.contourArea(cnt)

        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        rectArea = rect[1][0]*rect[1][1]

        if rectArea*9 > imageArea:

            # rotate the image
            picRectAngle = rect[2] + 90
            if picRectAngle>=70:
                picRectAngle = picRectAngle - 90
            elif 20 < picRectAngle < 70:
                picRectAngle = 0

            rot = cv2.getRotationMatrix2D((w/2, h/2), picRectAngle, 1)
            result_img = cv2.warpAffine(copy.deepcopy(image), rot, (w, h), flags=cv2.INTER_LINEAR)

            # rotate points
            pts = np.int0(cv2.transform(np.array([box]), rot))[0]

            allXCord = [i[0] for i in pts]
            allYCord = [i[1] for i in pts]

            topLeftX, topLeftY = int(min(allXCord)), int(min(allYCord))
            bottomRightX, bottomRightY = int(max(allXCord)), int(max(allYCord))
            
            img_crop = result_img[topLeftY:bottomRightY, topLeftX:bottomRightX]

            os.makedirs(imageFolderOutputPath, exist_ok=True)
            
            fileName = os.path.split(imageInputPath)[1]
            newFileName = fileName.split(".")[0] + " - " + str(i) + ".jpg"
            newImagePath = os.path.join(imageFolderOutputPath, newFileName)
            
            cv2.imwrite(newImagePath, img_crop)

            i = i + 1

def addDateTest(imageInputPath, newDate):
            
    try:
        if dateData[subDirName] != "Unknown":

            exif_dict = piexif.load(imageInputPath)
            # newdate = dateData[subDirName]
            
            newExifDate = datetime.strptime(newdate, '%d/%m/%Y')
            newExifDate = newExifDate.strftime('%Y:%m:%d %H:%M:%S')
            
            exifDateToday = datetime.today()
            exifDateToday = exifDateToday.strftime('%Y:%m:%d %H:%M:%S')

            exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = newExifDate
            exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = exifDateToday
            
            exif_bytes = piexif.dump(exif_dict)
            piexif.insert(exif_bytes, imagePath)
            
    except:
        continue
    