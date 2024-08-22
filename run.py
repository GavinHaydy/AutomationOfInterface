"""
    @Author: Gavin
    @Email: bugpz2779@gmail.com theruffian@163.com
    @Blog: 'https://blog.csdn.net/BUGPZ'
    @StackOverFlow: 'https://stackoverflow.com/users/12850648/theruffian'
    @Github: 'https://github.com/GavinHaydy'
"""
import unittest
from GavinReportPro.core.testRunner import TestRunner
import os
# from testcase.test_web import TestBaidu
import time
import smtplib  # 邮件库
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart


now = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
report_time = time.strftime('%Y-%m-%d-%H.%M.%S', time.localtime(time.time()))
current_path = os.getcwd()  # 获取当前路径
case_path = os.path.join(current_path, 'TestCate')  # 用例路径 可以多个
report_path = os.path.join(current_path, 'Report')  # 结果报告存放路径


"""
    加载用例的方式一
    def run_all_case():
    discover = unittest.defaultTestLoader.discover(case_path, pattern='test_web.py')
    return discover
"""
"""
    加载用例的方式二： 放在with open 上方
    testsuite = unittest.Testsuite()
    testsuite.addTest(unittest.TestLoader.loadTestFromTestCase(用例类名))
"""
"""
    加载方式三：
    testsuite = unittest.Testsuite()
    testsuite.addTest(类名('函数名'))
"""


if __name__ == '__main__':
    runner = TestRunner(
        unittest.defaultTestLoader.discover('./case/', '*.py'),
        filename='report.html',
        report_dir='./Report',
        templates=3
    )
    runner.run()


