Memories
======

[![PyPi](https://img.shields.io/pypi/v/memories.svg)](https://pypi.org/project/memories/)
[![Documentation Status](https://readthedocs.org/projects/memories/badge/?version=latest)](https://memories.readthedocs.io/en/latest/?badge=latest)
[![License](https://img.shields.io/github/license/veedata/album-manager)](https://github.com/veedata/album-manager/blob/main/LICENSE.txt)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/github/veedata/album-manager)](https://lgtm.com/projects/g/veedata/album-manager/context:python)
[![Downloads](https://pepy.tech/badge/memories)](https://pepy.tech/project/memories)

Description
------

Memories is an easy to use package that helps to seperate clustered images from files and helps add metadata to files. The documentation is in progress and can be found [here](https://memories.readthedocs.io/en/latest).

Installation
------

    $ pip install memories

How to Use:
------
There are 7 functions at the time being:
* ``open_image``: Returns the Image object to you so that it can be passed around to other functions
* ``divided_crop``: Takes 3 inputs, the path to the image, the path where the outful folder should be and the number of images present in the input file. It performs the task of dividing a single image into multiple smaller ones. 
* ``add_date``: Takes input as the image path and the datetime to be added. it will add date when the image was originally taken.
* ``bulk_add_date``: Same as addDate, except it will add date to all images in a folder. The inputs are the folder path and datetime.
* ``save_pdf``: Converts a list of images (one or more) into a PDF
* ``save_image``: Converts a single image into another format
* ``make_page``: Creates a year book like page in HTML
* ``make_border``: Creates a border around the image

Example
------
  
    import memories

    # Add meta data to images
    memories.add_date("./image-1.jpg", "27/04/2021 12:00:03")
    memories.bulk_add_date("./", "27/04/2021 12:00:03")
 
    memories.make_page(["./source_folder/image1.png", "./random/another_source_folder/image2.jpg"], ["CSS", "Larry"], ["SASS", "That one got to you, didnt it"], "./save_folder")

    image = memories.open_image("./image.png")

    memories.divided_crop(image, image_quantity = 6, bgr_value = [255, 255, 255])
    # Normal squared borders
    memories.make_border(image, "normal", bgr_value = [255, 255, 255], border_dimensions = [100, 100, 100, 100])
    # Curved borders
    memories.make_border(image, "curved", bgr_value = [255, 255, 255], border_dimensions = [100, 100, 100, 100], radius_dimensions = [100, 100, 100, 100])

    memories.save_image("image.png", "path/to/save_folder/file.extention")
    # Save multiple images at once
    memories.save_image(["img-1.png", "img-1.jpg", "img-2.jpg"], "path/to/save_folder/file.extention")
    # Save multiple images as a pdf
    memories.save_pdf(["img-1.png", "img-1.jpg", "img-2.jpg"], "path/to/save_folder/file.pdf")



Features
------

Current features that are present are: 
1. Crop out basic implementation
2. Add Date and time metadata 
3. Save as PDF, PNG, JPG
4. Basic Scrapbook implmentation
5. Documentation
6. Border

Future features can also be found at [Featuers](https://github.com/veedata/album-manager/projects):
1. Collage
2. Image Age identifyer

License
------
This software is released under the MIT license, see [LICENSE.txt](https://github.com/veedata/album-manager/blob/main/LICENSE.txt).
