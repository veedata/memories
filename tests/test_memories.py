import unittest
import os

import memories as mem


class test_image_loading(unittest.TestCase):
    def test_open_local_image(self):
        img = mem.open_image(
            os.path.join(os.path.dirname(__file__), 'test_images',
                         'memories_template.png'))
        self.assertEqual(img.shape, (2339, 1654, 3))

    def test_open_online_image(self):
        img = mem.open_image(
            r'https://github.com/veedata/memories/blob/main/tests/test_images/memories_template.png?raw=true'
        )
        self.assertEqual(img.shape, (2339, 1654, 3))


class test_operations(unittest.TestCase):
    def test_normal_borders(self):
        img = mem.open_image(
            os.path.join(os.path.dirname(__file__), 'test_images',
                         'memories_template.png'))
        img_bordered = mem.make_border(img,
                                       border_type="normal",
                                       bgr_value=[255, 0, 0, 255],
                                       border_dimension=10)
        self.assertEqual(img_bordered.shape, (2359, 1674, 3))

    def test_curved_borders(self):
        img = mem.open_image(
            os.path.join(os.path.dirname(__file__), 'test_images',
                         'memories_template.png'))
        img_bordered = mem.make_border(img,
                                       border_type="curved",
                                       bgr_value=[255, 0, 0, 255],
                                       border_dimension=10)
        self.assertEqual(img_bordered.shape, (2359, 1674, 4))
