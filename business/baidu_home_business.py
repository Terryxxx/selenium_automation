# -*- encoding: utf-8 -*-
'''
@File    :   baidu_home_business.py
@Time    :   2019/03/11 16:33:19
@Author  :   Terry Xu
'''
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from base.base_view import BaseWebPage
from page.baidu_home_page import BaiDuHomePage

class HomeBusiness(BaseWebPage):
    def __init__(self, driver):
        self._page = BaiDuHomePage()
        super(HomeBusiness, self).__init__(driver=driver)
    
    def search_by_text(self, text):
        self.send_keys(self._page.search_input, text)
        self.click(self._page.submit_button)
