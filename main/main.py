# coding=utf-8

import os
import time
import unittest
from cases.helper.HTMLTestRunner import HTMLTestRunner
from cases.login_case import LoginTestCase
from cases.modify_password_case import ModifyPasswordTestCase
from cases.splash_case import SplashTestCase
from cases.main_case import MainTestCase
from cases.helper.utils import del_current_day_log, del_current_day_image


# 生成报告相关参数
# report_file_name = r'report\test_report.html'
report_title = u'自动化测试报告'
report_description = u'用例执行情况'

path = '..\\cases'
result = '..\\result\\'


def get_test_case(clazz, test_case_list=None, prefix='test_'):
    """
    添加指定测试类中的测试用例
    :param clazz:
    :param test_case_list:
    :return []:
    """
    method_list = dir(clazz)
    for method in method_list:
        if method.startswith(prefix):
            test_case_list.append(clazz(method))


def generate_test_suite(prefix='test_'):
    """
    添加测试用例，并生成TestSuite对象
    :return TestSuite:
    """
    test_suit = unittest.TestSuite()
    # 存储测试用例的列表
    test_case_list = []
    # 添加login模块的测试用例
    # get_test_case(LoginTestCase, test_case_list, prefix)
    # 添加闪屏页模块的测试用例
    # get_test_case(SplashTestCase, test_case_list)
    # 添加重置密码模块的测试用例
    # get_test_case(ModifyPasswordTestCase, test_case_list)
    # 添加主界面模块的测试用例
    get_test_case(MainTestCase, test_case_list)
    for case in test_case_list:
        test_suit.addTest(case)

    return test_suit


def create_suite(case_path):
    # 定义单元测试容器
    test_suite = unittest.TestSuite()

    # 定搜索用例文件的方法
    cases = unittest.defaultTestLoader.discover(case_path, pattern='*_case.py', top_level_dir=None)

    # 将测试用例加入测试容器中
    for case in cases:
        for case_name in case:
            test_suite.addTest(case_name)
        print test_suite
    return test_suite


# 测试之前先删除当天日志
del_current_day_log()
# 删除当天的图片
del_current_day_image()

# 设置是否只测试目标单元测试
is_just_test_target_case = True

if is_just_test_target_case:
    test_case = generate_test_suite()
else:
    is_test_order = True  # 是否按指定测试用例执行
    if is_test_order:
        test_case = generate_test_suite()
    else:
        test_case = create_suite(path)

# 设置是否显示在终端：True在终端显示， False通过html报告显示
is_show_on_terminal = True
if is_show_on_terminal:
    unittest.TextTestRunner(verbosity=2).run(test_case)
else:
    # 获取系统当前时间
    now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    day = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    # 定义报告存放路径，支持相对路径
    test_result_dir = result + day

    if not os.path.exists(test_result_dir):
        os.mkdir(test_result_dir)

    filename = test_result_dir + '\\' + now + '_result.html'
    fp = file(filename, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp, title=report_title, description=report_description)

    # 运行测试用例
    runner.run(test_case)
    # 关闭报告文件
    fp.close()
