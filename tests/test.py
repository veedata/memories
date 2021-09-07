import unittest
import os
import numpy as np

import memories as mem


class test_memories(unittest.TestCase):
    def test_open_image(self):
        img = mem.open_image(os.path.join(os.path.dirname(__file__), 'test_images', 'obama.jpg'))
        self.assertEqual(img.shape, (2339, 1654, 3))
