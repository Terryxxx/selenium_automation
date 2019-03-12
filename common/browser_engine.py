# -*- encoding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.base_log import Log
from utils.read_yaml import YamlReader
'''
@File    :   browser_engine.py
@Time    :   2019/03/11 16:21:06
@Author  :   Terry Xu
'''

import os
import sys
from selenium import webdriver
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

base_dir = os.path.dirname(os.path.dirname(__file__))
driver_path = os.path.join(base_dir, 'drivers')
logging = Log().get_logger()
TYPES = {
    'firefox': webdriver.Firefox,
    'chrome': webdriver.Chrome,
    'ie': webdriver.Ie,
    'phantomjs': webdriver.PhantomJS,
    'headless': webdriver.Chrome
}


class Browser():
    def __init__(self):
        yaml_file = os.path.join(base_dir, 'config', 'config.yaml')
        self._type = YamlReader(yaml_file).get('browser').lower()
        if self._type in TYPES:
            self.browser = TYPES[self._type]
        else:
            raise Exception('仅支持%s!' % ', '.join(TYPES.keys()))
        self.url = YamlReader(yaml_file).get('local_url')
        self.driver = None

    def open_browser(self):
        if sys.platform == "darwin":
            chrome_path = os.path.join(driver_path, 'mac/chromedriver')
        elif sys.platform == "Windows":
            chrome_path = os.path.join(base_dir, 'windows/chromedriver')

        if self._type == 'headless':
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            self.driver = self.browser(executable_path=chrome_path, chrome_options=options)
        else:
            self.driver = self.browser(executable_path=chrome_path)

        logging.info('Open website {}'.format(self.url))
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(5)
        return self.driver


if __name__ == "__main__":
    driver = Browser().open_browser()
    driver.close()
    driver.quit()
