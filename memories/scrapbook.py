import os
import logging
import sys


def make_page(image_list: list, name_list: list, tag_list: list, output_path: str):
    """Save a list of images in PDF format

    :param image_list: List of path to all images to be put in the HTML
    :type image_list: list
    :param name_list: List of names to be put in the HTML
    :type name_list: list
    :param tag_list: List of short line put in the HTML
    :type tag_list: list
    :param output_path: save path to the folder
    :type output_path: str
    """

    if not(len(image_list) == len(name_list) == len(tag_list)):
        logging.error("The lengths of the inputs differ")
        sys.exit(1)

    output_file_path = os.path.join(output_path, 'scrapbook.html')
    f = open(output_file_path, 'w')

    dynamic_text = ""

    for i in range(len(image_list)):
        template_segment_text = f'''
            <div class="col">
                <div class="card h-100 border-primary">
                    <div style="padding: 1em;">
                        <img src="{image_list[i]}" class="rounded-3 card-img-top" alt="...">
                    </div>
                    <div class="card-body">
                        <h5 class="card-title">{name_list[i]}</h5>
                        <p class="card-text">{tag_list[i]}</p>
                    </div>
                </div>
            </div>'''
        dynamic_text = dynamic_text + template_segment_text

    static_text = f"""
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
                        {dynamic_text}
                    </div>
                </div>

                <br>
                <br>

            </body>

            </html>
        """

    f.write(static_text)
    f.close()
