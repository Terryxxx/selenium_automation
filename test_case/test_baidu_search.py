# -*- encoding: utf-8 -*-

'''
@File    :   test_baidu_search.py
@Time    :   2019/03/11 16:39:18
@Author  :   Terry Xu
'''
import time
import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from BeautifulReport.BeautifulReport import BeautifulReport
from business.baidu_home_business import HomeBusiness
from common.browser_engine import open_browser
from utils.base_runner import BaseWebTestCase

class TestBaiDuSearch(BaseWebTestCase):
    
    @BeautifulReport.add_test_img('test_baidu_search_{}'.format(time.strftime('%Y%m%d%H%M%S')))
    def test_baidu_search(self):
        self.home = HomeBusiness(self.web_driver)
        self.home.search_by_text('中国')
    
    @BeautifulReport.add_test_img('test_baidu_search_fail_{}'.format(time.strftime('%Y%m%d%H%M%S')))
    def test_baidu_search_fail(self):
        self.home = HomeBusiness(self.web_driver)
        self.home.search_by_text('中国')
        assert 1 == 2
