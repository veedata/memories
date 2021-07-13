Memories
======

[![PyPi](https://img.shields.io/pypi/v/memories.svg)](https://pypi.org/project/memories/)
[![Documentation Status](https://readthedocs.org/projects/memories/badge/?version=latest)](https://memories.readthedocs.io/en/latest/?badge=latest)
[![License](https://img.shields.io/github/license/veedata/album-manager)](https://github.com/veedata/album-manager/blob/main/LICENSE.txt)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/github/veedata/album-manager)](https://lgtm.com/projects/g/veedata/album-manager/context:python)
[![Downloads](https://pepy.tech/badge/memories)](https://pepy.tech/project/memories)

Description
------

Memories is an easy to use package that helps to seperate clustered images from files and helps add metadata to files. The documentation is in progress and will be present in the "``docs``" directory of the project in the future. For the time being the following steps should be an adequate description of all functions present.

Installation
------

    $ pip install memories

How to Use:
------
There are 6 functions at the time being:
* ``dividedCrop``: Takes 3 inputs, the path to the image, the path where the outful folder should be and the number of images present in the input file. It performs the task of dividing a single image into multiple smaller ones. 
* ``addDate``: Takes input as the image path and the datetime to be added. it will add date when the image was originally taken.
* ``bulkAddDate``: Same as addDate, except it will add date to all images in a folder. The inputs are the folder path and datetime.
* ``saveAsPDF``: Converts a list of images (one or more) into a PDF
* ``saveAs``: Converts a single image into another format
* ``makePage``: Creates a year book like page in HTML

Example
------
  
    import memories

    memories.dividedCrop("./image.png", "./", imageQuantity = 6, bgrVal = [255, 255, 255])
    memories.addDate("./image-1.jpg", "27/04/2021 12:00:03")
    memories.bulkAddDate("./", "27/04/2021 12:00:03")
    memories.saveAsPDF(["./source_folder/image1.png", "./random/another_source_folder/image2.jpg"], "./save_folder/file.pdf")
    memories.saveAs("./source_folder/image1.jpg", ".png")
    memories.makePage(["./source_folder/image1.png", "./random/another_source_folder/image2.jpg"], ["CSS", "Larry"], ["SASS", "That one got to you, didnt it"], "./save_folder")


Features
------

Current features that are present are: 
1. Crop out basic implementation
2. Add Date and time metadata 
3. Save as PDF, PNG, JPG
4. Basic Scrapbook implmentation
5. Documentation

Future features can also be found at https://github.com/veedata/album-manager/projects/1:
1. Border
2. Collage
3. Image Age identifyer

License
------
This software is released under the MIT license, see [LICENSE.txt](https://github.com/veedata/album-manager/blob/main/LICENSE.txt).
