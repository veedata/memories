===============
Getting started
===============

Installation
------------

Install the Python package::

    pip install memories


How to Use
----------

There are 6 functions at the time being:

- ``dividedCrop``: Takes 3 inputs, the path to the image, the path where the outful folder should be and the number of images present in the input file. It performs the task of dividing a single image into multiple smaller ones. 
- ``addDate``: Taken input as the image path and the datetime to be added. it will add date when the image was originally taken.
- ``bulkAddDate``: Same as addDate, except it will add date to all images in a folder. The inputs are the folder path and datetime.
- ``saveAsPDF``: Converts a list of images (one or more) into a PDF
- ``saveAs``: Converts a single image into another format
- ``makePage``: Creates a year book like page in HTML


Example
-------

An example code for each appplication::

    import memories

    memories.dividedCrop("./image.png", "./", 4)
    memories.addDate("./image-1.jpg", "27/04/2021 12:00:03")
    memories.bulkAddDate("./", "27/04/2021 12:00:03")
    memories.saveAsPDF(["./source_folder/image1.png", "./random/another_source_folder/image2.jpg"], "./save_folder/file.pdf")
    memories.saveAs("./source_folder/image1.jpg", ".png")
    memories.makePage(["./source_folder/image1.png", "./random/another_source_folder/image2.jpg"], ["CSS", "Larry"], ["SASS", "That one got to you, didnt it"], "./save_folder")


License
-------
This software is released under the MIT license, see `LICENSE.txt <https://github.com/veedata/album-manager/blob/main/LICENSE.txt>`_.
