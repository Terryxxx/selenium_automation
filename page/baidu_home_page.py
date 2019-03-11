# -*- encoding: utf-8 -*-
'''
@File    :   baidu_home_page.py
@Time    :   2019/03/11 16:31:44
@Author  :   Terry Xu
'''

from selenium.webdriver.common.by import By


class BaiDuHomePage(object):
    search_input = (By.ID, 'kw')
    submit_button = (By.ID, 'su')