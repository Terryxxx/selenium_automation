# -*- encoding: utf-8 -*-
'''
@File    :   base_view.py
@Time    :   2019/03/11 16:34:11
@Author  :   Terry Xu
'''
import logging
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class BaseWebPage(object):
    def __init__(self, driver):
        self.driver = driver

    def quit_browser(self):
        self.driver.quit()

    def find_element(self, *loc):
        logging.info('Find element by %s: %s' % (loc[0], loc[1]))
        try:
            element = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(locator=loc))
            return element
        except NoSuchElementException:
            logging.error('Can not find element: %s' % loc[1])
            raise
        except TimeoutException:
            logging.error('Can not find element: %s' % loc[1])
            raise

    def find_elements(self, *loc):
        logging.info('Find element by %s: %s' % (loc[0], loc[1]))
        try:
            elements = WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located(locator=loc))
            return elements
        except NoSuchElementException:
            logging.error('Can not find element: %s' % loc[1])
            raise

    def find_element_by_text(self, loc, text):
        try:
            elements = self.find_elements(*loc)
            for element in elements:
                if text in element.text:
                    return element
        except:
            raise

    def click(self, loc):
        try:
            self.find_element(*loc).click()
            logging.info('Click element by %s: %s...' % (loc[0], loc[1]))
            time.sleep(1)
        except AttributeError:
            raise

    def clicks(self, loc, index):
        try:
            element = self.find_elements(*loc)[index]
            element.click()
            logging.info('Click element by %s: %s...' % (loc[0], loc[1]))
            time.sleep(1)
        except AttributeError:
            raise

    def send_keys(self, loc, text, need_clear=False):
        try:
            element = self.find_element(*loc)
            element.click()
            if need_clear:
                element.clear()
            logging.info('Send keys %s' % text)
            element.send_keys(text)
        except AttributeError:
            raise

    def send_keys_by_index(self, loc, text, index, need_clear=False):
        try:
            element = self.find_elements(*loc)[index]
            element.click()
            if need_clear:
                element.clear()
            logging.info('Send keys %s' % text)
            element.send_keys(text)
        except AttributeError:
            raise

    def switch_to_window_by_title(self, title):
        time.sleep(2)
        handles = self.driver.window_handles
        for i in range(len(handles)):
            self.driver.switch_to.window(handles[i])
            current_title = self.driver.title
            if title in current_title:
                break
        time.sleep(2)

    def switch_to_window_by_index(self, index):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[index])

    def get_current_window_handle(self):
        return self.driver.current_window_handle

    def close_window_by_title(self, current_handle):
        all_handles = self.driver.window_handles

        for window in all_handles:
            if window != current_handle:
                self.driver.switch_to.window(window)
                self.driver.close()
        self.driver.switch_to.window(current_handle)

    def switch_to_frame(self, frame):
        self.driver.switch_to.frame(frame)

    def switch_to_parent_frame(self):
        self.driver.switch_to.parent_frame()

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()
