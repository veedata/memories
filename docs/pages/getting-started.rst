===============
Getting started
===============

Requirements
------------

- Python 3.6+


Installation
------------

Install the Python package::

    pip install memories


How to Use
----------

There are 7 functions at the time being:

- ``open_image``: Open an image as a numpy array
- ``divided_crop``: Takes 3 inputs, the path to the image, the path where the outful folder should be and the number of images present in the input file. It performs the task of dividing a single image into multiple smaller ones. 
- ``add_date``: Takes input as the image path and the datetime to be added. it will add date when the image was originally taken.
- ``bulk_add_date``: Same as addDate, except it will add date to all images in a folder. The inputs are the folder path and datetime.
- ``save_pdf``: Converts a list of images (one or more) into a PDF
- ``save_image``: Converts a single image into another format
- ``make_page``: Creates a year book like page in HTML
- ``make_border``: Creates a border around the image


Example
-------

An example code for each appplication::

.. code-block:: python

    import memories

    # Add date to images
    memories.add_date("./image-1.jpg", "27/04/2021 12:00:03")
    memories.bulk_add_date("./", "27/04/2021 12:00:03")
 
    memories.make_page(["./source_folder/image1.png", "./random/another_source_folder/image2.jpg"], ["CSS", "Larry"], ["SASS", "That one got to you, didnt it"], "./save_folder")

    image = memories.open_image("./image.png")
    image1 = mem.open_image("./image.png")
    image2 = mem.open_image("./image.png")
    image3 = mem.open_image("./image.png")

    memories.divided_crop(image, image_quantity = 6, bgr_value = [255, 255, 255])
    # Normal squared borders
    memories.make_border(image, "normal", bgr_value = [255, 255, 255], border_dimensions = [100, 100, 100, 100])
    # Curved borders
    memories.make_border(image, "curved", bgr_value = [255, 255, 255], border_dimensions = [100, 100, 100, 100], radius_dimensions = [100, 100, 100, 100])

    memories.save_image(image, "path/to/save_folder/file.extention")
    # Save multiple images at once
    memories.save_image([image1, image2, image3], "path/to/save_folder/file.extention")
    # Save multiple images as a pdf
    memories.save_pdf(["img-1.png", "img-1.jpg", "img-2.jpg"], "path/to/save_folder/file.pdf")
