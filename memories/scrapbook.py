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
            <html>
            <head>
            </head>
            <body>
                <p>Hello World!</p>
                </body>
            </html>
        """

    f.write(staticText)
    f.close()