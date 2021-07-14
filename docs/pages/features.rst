Features
========

Divide Image groups 
-------------------

Converting hard copies of images into their soft copies usually leads to more than a single image being scanned on the same page. And while many devices have an inbuilt option to divide that scan into multiple images, some don't. This module has been built keeping that scenario in mind. The module divides a scan into it's member images based on background color also if provided. 

.. automodule:: memories.divider
    :members:
    :undoc-members:
    :show-inheritance:

Add meta data to images
-----------------------

Allows the addition of metadata to images (only jpg supported). The feature currently only provides addition of Date metadata but will be updated in the future with more options.

.. automodule:: memories.meta
    :members:
    :undoc-members:
    :show-inheritance:

Save in other formats
---------------------

Easy conversion of an image into other formats. Currently supported input and output formats can be found `here <https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html>`_. Additionally saving to pdf can be performed, where pdf saves multiple input images in a single pdf file.

.. automodule:: memories.save_as
    :members:
    :undoc-members:
    :show-inheritance:

Scrapbook
---------

On input of name, short line and image, this function generates a year-book like webpage.

.. automodule:: memories.scrapbook
    :members:
    :undoc-members:
    :show-inheritance: