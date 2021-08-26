import os
import logging
import sys


def makePage(imageList: list, nameList: list, tagList: list, outputPath: str):
    """Save a list of images in PDF format

    :param imageList: List of path to all images to be put in the HTML
    :type imageList: list
    :param nameList: List of names to be put in the HTML
    :type nameList: list
    :param tagList: List of short line put in the HTML
    :type tagList: list
    :param outputPath: save path to the folder
    :type outputPath: str
    """

    if not(len(imageList) == len(nameList) == len(tagList)):
        logging.error("The lengths of the inputs differ")
        sys.exit(1)

    outputFilePath = os.path.join(outputPath, 'scrapbook.html')
    f = open(outputFilePath, 'w')

    dynamicText = ""

    for i in range(len(imageList)):
        thisText = f'''
            <div class="col">
                <div class="card h-100 border-primary">
                    <div style="padding: 1em;">
                        <img src="{imageList[i]}" class="rounded-3 card-img-top" alt="...">
                    </div>
                    <div class="card-body">
                        <h5 class="card-title">{nameList[i]}</h5>
                        <p class="card-text">{tagList[i]}</p>
                    </div>
                </div>
            </div>'''
        dynamicText = dynamicText + thisText

    staticText = f"""
            <!doctype html>
            <html lang="en">

            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">

                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet"
                    integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">

                <title>A Scrapbook Page</title>
            </head>

            <body>
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.bundle.min.js"
                    integrity="sha384-gtEjrD/SeCtmISkJkNUaaKMoLD0//ElJ19smozuHV6z3Iehds+3Ulb9Bn9Plx0x4"
                    crossorigin="anonymous"></script>

                <br>
                <br>

                <div class="container">

                    <div class="row row-cols-1 row-cols-md-3 g-4">
                        {dynamicText}
                    </div>
                </div>

                <br>
                <br>

            </body>

            </html>
        """

    f.write(staticText)
    f.close()
