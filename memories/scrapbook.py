import os
import logging
import sys


def make_page(image_list: list, name_list: list, tag_list: list,
              output_path: str, template: str):
    """Generate HTML page from list of images

    Args:
        image_list (list): List of path to all images to be put in the HTML
        name_list (list): List of names to be put in the HTML
        tag_list (list): List of short line put in the HTML
        output_path (str): Save path to the folder
        template (str): Template name to use

    Todo:
        Add more templates
    """

    if not (len(image_list) == len(name_list) == len(tag_list)):
        logging.error("The lengths of the inputs differ")
        sys.exit(1)

    output_file_path = os.path.join(output_path, 'scrapbook.html')
    template_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 "html_templates", "template1.html")

    dynamic_text = ""

    for i in range(len(image_list)):
        template_segment_text = f'''
            <div class="col">
                <div class="card h-100 border-primary">
                    <div style="padding: 1em;">
                        <img src="{image_list[i]}"
                            class="rounded-3 card-img-top" alt="...">
                    </div>
                    <div class="card-body">
                        <h5 class="card-title">{name_list[i]}</h5>
                        <p class="card-text">{tag_list[i]}</p>
                    </div>
                </div>
            </div>'''
        dynamic_text = dynamic_text + template_segment_text

    with open(template_path, 'r') as file:
        filedata = file.read()

    filedata = filedata.replace(r'{dynamic_text}', dynamic_text)

    with open(output_file_path, 'w') as file:
        file.write(filedata)
