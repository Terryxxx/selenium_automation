# -*- encoding: utf-8 -*-
'''
@File    :   run_all_case.py
@Time    :   2019/03/11 16:59:31
@Author  :   Terry Xu
'''

import os
import sys
import time
import unittest
sys.path.append(os.path.dirname(__file__))
from BeautifulReport.BeautifulReport import BeautifulReport


base_dir = os.path.dirname(__file__)
report_path = os.path.join(base_dir, 'report')
case_path = os.path.join(base_dir, 'test_case')
test_suite1 = unittest.TestLoader().discover(case_path, pattern='test_*.py')
suite = unittest.TestSuite(test_suite1)
result = BeautifulReport(suite)
result.report(filename="web_baidu_test_" + time.strftime('%Y%m%d%H%M%S') + ".html",
              description='Web Automation Test Case',
              log_path=report_path)
