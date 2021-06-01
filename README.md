Memories
======

[![PyPi](https://img.shields.io/pypi/v/memories.svg)](https://pypi.org/project/memories/)
[![Downloads](https://pepy.tech/badge/memories)](https://pepy.tech/project/memories)
[![License](https://img.shields.io/github/license/veedata/album-manager)](https://github.com/veedata/album-manager/blob/main/LICENSE.txt)

Description
------

Memories is an easy to use package that helps to seperate clustered images from files and helps add metadata to files. The documentation is in progress and will be present in the "``docs``" directory of the project in the future. For the time being the following steps should be an adequate description of all functions present.

Installation
------

    $ pip install memories

How to Use:
------
There are 6 functions at the time being:
* ``memories.dividedCrop``: Takes 3 inputs, the path to the image, the path where the outful folder should be and the number of images present in the input file. It performs the task of dividing a single image into multiple smaller ones. 
* ``addDate``: Taken input as the image path and the datetime to be added. it will add date when the image was originally taken.
* ``bulkAddDate``: Same as addDate, except it will add date to all images in a folder. The inputs are the folder path and datetime.
* ``saveAsPDF``: Converts a list of images (one or more) into a PDF
* ``saveAsPNG``: Converts a single image into PNG format
* ``saveAsJPG``: Converts a single image into JPG format

Example
------
  
    import memories

    memories.dividedCrop("./image.png", "./", 4)
    memories.addDate("./image-1.jpg", "27/04/2021 12:00:03")
    memories.bulkAddDate("./", "27/04/2021 12:00:03")
    memories.saveAsPDF(["./source_folder/image1.png", "./random/another_source_folder/image2.jpg"], "./save_folder/file.pdf")
    memories.saveAsPNG("./source_folder/image1.jpg", "./output_folder")
    memories.saveAsJPG("./source_folder/image1.png", "./output_folder")


Features
------

Current features that are present are: 
1. Crop out basic implementation
2. Add Date and time metadata 
3. Save as PDF, PNG, JPG

Future features can also be found at https://github.com/veedata/album-manager/projects/1:
1. Border
2. Collage
3. Image Age identifyer
4. Documentation

License
------
This software is released under the MIT license, see [LICENSE.txt](https://github.com/veedata/album-manager/blob/main/LICENSE.txt).
