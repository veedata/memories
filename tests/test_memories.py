import unittest
import os
import imagehash
from PIL import Image

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
    @classmethod
    def setUpClass(cls):
        cls.base_path = os.path.join(os.path.dirname(__file__), 'test_images')
        cls.img = mem.open_image(
            os.path.join(cls.base_path, 'memories_template.png'))

    def test_normal_borders(self):
        img_bordered = mem.make_border(self.img,
                                       border_type="normal",
                                       bgr_value=[255, 0, 0, 255],
                                       border_dimension=10)
        self.assertEqual(img_bordered.shape, (2359, 1674, 3))

    def test_curved_borders(self):
        img_bordered = mem.make_border(self.img,
                                       border_type="curved",
                                       bgr_value=[255, 0, 0, 255],
                                       border_dimension=10)
        self.assertEqual(img_bordered.shape, (2359, 1674, 4))


class test_divider(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base_path = os.path.join(os.path.dirname(__file__), 'test_images')
        cls.img = mem.open_image(
            os.path.join(cls.base_path, 'memories_template.png'))

    def test_images_quantity(self):
        split_images = mem.divided_crop(self.img,
                                        image_quantity=5,
                                        bgr_value=[255, 255, 255])
        self.assertEqual(len(split_images), 5)

    def test_images_crop(self):

        def hash_check(image_hash):
            hash_list = []

            for i in range(1, 6):
                org_image = mem.open_image(
                    os.path.join(self.base_path, 'image' + str(i) + '.jpg'))
                org_hash = imagehash.average_hash(Image.fromarray(org_image))

                hash_list.append(org_hash - image_hash)

            return hash_list

        split_image = mem.divided_crop(self.img,
                                       image_quantity=5,
                                       bgr_value=[255, 255, 255])

        result_list = []
        for image in split_image:
            image_hash = imagehash.average_hash(Image.fromarray(image))

            hash_list = hash_check(image_hash)

            if min(hash_list) < 5:
                result_list.append(1)

        self.assertEqual(sum(result_list), 4)


class test_save_image(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base_path = os.path.join(os.path.dirname(__file__), 'test_images')

        cls.img_path = os.path.join(cls.base_path, 'memories_template.png')
        cls.img1_path = os.path.join(cls.base_path, 'image1.jpg')
        cls.img2_path = os.path.join(cls.base_path, 'image2.jpg')
        cls.img3_path = os.path.join(cls.base_path, 'image3.jpg')

        cls.img = mem.open_image(cls.img_path)
        cls.img1 = mem.open_image(cls.img1_path)
        cls.img2 = mem.open_image(cls.img2_path)
        cls.img3 = mem.open_image(cls.img3_path)

    def test_single_save_jpg(self):
        save_path = os.path.join(self.base_path, 'single_save.jpg')
        mem.save_image(self.img, save_path)
        self.assertTrue(os.path.join(self.base_path, 'single_save.png'))

    def test_single_save_png(self):
        save_path = os.path.join(self.base_path, 'single_save.png')
        mem.save_image(self.img, save_path)
        self.assertTrue(os.path.isfile(save_path))

    def test_multiple_save(self):
        save_path = os.path.join(self.base_path, 'multi_save.jpg')
        mem.save_image([self.img1, self.img2, self.img3], save_path)

        img1_save_path = os.path.join(self.base_path, 'multi_save-0.jpg')
        img2_save_path = os.path.join(self.base_path, 'multi_save-1.jpg')
        img3_save_path = os.path.join(self.base_path, 'multi_save-2.jpg')

        self.assertTrue(os.path.isfile(img1_save_path))
        self.assertTrue(os.path.isfile(img2_save_path))
        self.assertTrue(os.path.isfile(img3_save_path))

    def test_pdf_single_save(self):
        save_path = os.path.join(self.base_path, 'single_save.pdf')
        mem.save_pdf([self.img_path], save_path)
        self.assertTrue(os.path.isfile(save_path))

    def test_pdf_multi_save(self):
        mem.save_pdf([self.img1_path, self.img2_path, self.img3_path],
                     os.path.join(self.base_path, 'multi_save.pdf'))
        self.assertTrue(os.path.join(self.base_path, 'multi_save.pdf'))

    @classmethod
    def tearDownClass(self):
        os.remove(os.path.join(self.base_path, 'single_save.jpg'))
        os.remove(os.path.join(self.base_path, 'single_save.png'))
        os.remove(os.path.join(self.base_path, 'multi_save-0.jpg'))
        os.remove(os.path.join(self.base_path, 'multi_save-1.jpg'))
        os.remove(os.path.join(self.base_path, 'multi_save-2.jpg'))
        os.remove(os.path.join(self.base_path, 'single_save.pdf'))
        os.remove(os.path.join(self.base_path, 'multi_save.pdf'))
