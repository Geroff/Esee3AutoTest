# coding=utf-8

import unittest
from helper.HTMLTestRunner import HTMLTestRunner
from cases.login_case import LoginTestCase
from cases.main_case import MainTestCase

# 生成报告相关参数
report_file_name = r'report\test_report.html'
report_title = u'自动化测试报告'
report_description = u'显示自动化测试报告结果'


def get_test_case(clazz, test_case_list=None):
    """
    添加指定测试类中的测试用例
    :param clazz:
    :param test_case_list:
    :return []:
    """
    method_list = dir(clazz)
    for method in method_list:
        if method.startswith("test_"):
            test_case_list.append(clazz(method))


def generate_test_suite():
    """
    添加测试用例，并生成TestSuite对象
    :return TestSuite:
    """
    test_suit = unittest.TestSuite()
    # 存储测试用例的列表
    test_case_list = []
    # 添加login模块的测试用例
    get_test_case(LoginTestCase, test_case_list)
    # 添加main模块的测试用例
    get_test_case(MainTestCase, test_case_list)
    for test_case in test_case_list:
        test_suit.addTest(test_case)

    return test_suit


# ===============测试所有测试用例的时候用=============
# suit = generate_test_suite()
# ================================================

# ===============单独测试某个用例的时候用=============
suit = unittest.TestSuite()
# suit.addTest(MainTestCase('test_is_device_dialog_show'))
# suit.addTest(MainTestCase('test_get_window_size'))
# suit.addTest(LoginTestCase('test_user_password_hint_text_is_correct'))
suit.addTest(LoginTestCase('test_view_color'))
# ================================================

# ===============直接终端查看结果的时候用=============
# unittest.TextTestRunner(verbosity=2).run(suit)
# ================================================

# ===============生成html报告的时候用=============
with open(report_file_name, 'wb') as test_report_file:
    # 生成html的测试报告
    runner = HTMLTestRunner(stream=test_report_file,
                            title=report_title,
                            description=report_description)
    runner.run(suit)
# ================================================
