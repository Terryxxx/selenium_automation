# -*- encoding: utf-8 -*-
'''
@File    :   browser_engine.py
@Time    :   2019/03/11 16:21:06
@Author  :   Terry Xu 
'''

import os
import sys
from selenium import webdriver
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.base_log import Log

logging = Log().get_logger()


def open_browser():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    driver_path = os.path.join(base_dir, 'drivers')
    if sys.platform == "darwin":
        chrome_path = os.path.join(driver_path, 'mac/chromedriver')
    elif sys.platform == "Windows":
        chrome_path = os.path.join(base_dir, 'windows/chromedriver')

    driver = webdriver.Chrome(executable_path=chrome_path)
    url = 'https://www.baidu.com/'
    logging.info('Open website {}'.format(url))
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver


if __name__ == "__main__":
    driver = open_browser()
    driver.close()
    driver.quit()
