import os
import logging

def makePage(imageList: list, nameList: list, tagList: list):
    """Save a list of images in PDF format

    @type imageList: list
    @param imageList: List of path to all images to be put in the HTML
    @type nameList: list
    @param nameList: List of names to be put in the HTML    
    @type tagList: list
    @param tagList: List of short line put in the HTML
    """

    if len(imageList) == len(nameList) == len(tagList):
        pass
    else:
        logging.error("Oof, input lengths aint same")

    f = open('scrapbook.html', 'w')

    dynamicText = ""
    # To Do, a lot to do
    for i in len(imageList):
        dynamicText = dynamicText + imageList[i]

    staticText = """
            <!doctype html>
            <html lang="en">

            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">

                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet"
                    integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">

                <title>A Scrapbook Page</title>

                <!-- <style>
                    html, body {
                        height:297mm;
                        width:210mm;
                    }
                </style> -->
            </head>

            <body>
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.bundle.min.js"
                    integrity="sha384-gtEjrD/SeCtmISkJkNUaaKMoLD0//ElJ19smozuHV6z3Iehds+3Ulb9Bn9Plx0x4"
                    crossorigin="anonymous"></script>

                <div class="container">

                    <div class="row row-cols-1 row-cols-md-3 g-4">
                        <div class="col">
                            <div class="card h-100">
                                <img src="image_path" class="card-img-top rounded-2" alt="...">
                                <div class="card-body">
                                    <h5 class="card-title">Person Name</h5>
                                    <p class="card-text">A short one-line.</p>
                                </div>
                            </div>
                        </div>
                </div>
            </body>

            </html>
        """

    f.write(staticText)
    f.close()