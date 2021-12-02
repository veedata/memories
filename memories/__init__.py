__version__ = "1.0.1"


from .divider import divided_crop
from .divider import rotate_image

from .meta import add_date
from .meta import bulk_add_date
from .meta import add_date_png

from .save_as import open_image
from .save_as import save_image

from .scrapbook import make_page

from .border import make_border

__all__ = [
    "divided_crop", "add_date", "bulk_add_date", "add_date_png", "open_image",
    "save_image", "make_page", "make_border", "rotate_image"
]
