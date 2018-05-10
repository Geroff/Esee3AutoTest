# coding=utf-8

import unittest
from helper.ui_helper import UiHelper


class BaseCase(unittest.TestCase):
    """
    测试类的基类
    """

    def setUp(self):
        """
        所有测试用例开始之前调用
        """
        self.uiHelper = UiHelper("..\main\deviceConfig.txt")
        self.uiHelper.init_driver()
        print("setUp")

    def tearDown(self):
        """
        所有测试用例结束之后调用
        """
        self.uiHelper.quit_driver()
        print("tearDown")


if __name__ == '__main__':
    unittest.main()
