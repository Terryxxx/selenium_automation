# -*- encoding: utf-8 -*-
from common.browser_engine import open_browser
'''
@File    :   base_runner.py
@Time    :   2019/03/11 17:11:55
@Author  :   Terry Xu
'''
import os
import unittest
import warnings

base_dir = os.path.dirname(os.path.dirname(__file__))


class BaseWebTestCase(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        warnings.simplefilter("ignore", DeprecationWarning)
        self.web_driver = open_browser()

    def tearDown(self):
        self.web_driver.close()
        self.web_driver.quit()

    def save_img(self, img_name):
        img_path = os.path.join(base_dir, 'img')
        self.web_driver.get_screenshot_as_file(
            '{}/{}.png'.format(img_path, img_name))
