Usage
=====

The following section shows a simple approach to be able 

Divide Image groups 
-------------------

Divide a image of images into multiple seperate images

.. code-block:: python

    import memories as mem

    mem.dividedCrop("./image.png", "./", imageQuantity = 6, bgrVal = [255, 255, 255])

Add borders to images 
---------------------

Automatically add borders to images. Borders will be added outisde the image and no image content will be cropped.

* borderDimensions = [top-border, bottom-border, left-border, right-border]
* radiusDimensions = [top-left, top-right, bottom-left, bottom-right]

.. code-block:: python

    import memories as mem

    # Making a simple border. 
    mem.makeBorder("./image.png", "normal", bgrVal = [255, 255, 255], borderDimensions = [100, 100, 100, 100])
    # Making a border with curved edges.
    mem.makeBorder("./image.png", "curved", bgrVal = [255, 255, 255], borderDimensions = [100, 100, 100, 100], radiusDimensions = [100, 100, 100, 100])


Generate HTML page
------------------

Allows for generation of HTML page from the input images and text. think of it like an uatogenerated scrapbook of sorts.

.. code-block:: python

    import memories as mem

    mem.makePage(["./source_folder/image1.png", "./random/another_source_folder/image2.jpg"], ["CSS", "Larry"], ["SASS", "That one got to you, didnt it"], "./save_folder")


Add metadata
------------

You can even add metadata to images duirectly from the module. (Only works for jpg images currently, future support for png is planned) 

.. code-block:: python

    import memories as mem

    # Add date to a single image using image path
    mem.addDate("./image-1.jpg", "27/04/2021 12:00:03")
    # Add date to images in bulk using folder path
    mem.bulkAddDate("./", "27/04/2021 12:00:03")
    

Save file
---------

The save as pdf function takes a list of images as input and produces a pdf with all those images in it, while the normal ``saveAs`` function is a simple adoption of PIL's save function.

.. code-block:: python

    import memories as mem

    mem.saveAsPDF(["./source_folder/image1.png", "./random/another_source_folder/image2.jpg"], "./save_folder/file.pdf")
    mem.saveAs("./source_folder/image1.jpg", ".png")
