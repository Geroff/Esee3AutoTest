# coding=utf-8

import unittest
import os

from PO.base_page import BasePage
# 此模块需要安装Appium-Python-Client
from appium import webdriver

# returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class BaseCase(unittest.TestCase):
    """
    测试类的基类
    """

    def setUp(self):
        """
        所有测试用例开始之前调用
        """
        desired_caps = {}
        remote_host = "http://127.0.0.1:4723/wd/hub"
        self.time_out = 10
        # 获取设备配置
        with open('..\\cases\\data\\deviceConfig.txt') as file_object:
            for line in file_object:
                if line.startswith("#"):
                    continue

                line = line.strip()
                words = line.split("=")
                if len(words) != 2:
                    continue

                if words[0] == 'app':
                    print(PATH(words[1]))
                    desired_caps[words[0]] = PATH(words[1])
                elif words[0] == 'remoteHost':
                    remote_host = words[1]
                else:
                    desired_caps[words[0]] = words[1]

        self.driver = webdriver.Remote(remote_host, desired_caps)

        self.is_in_expected_page = False
        BasePage.save_log("\n====================setUp=====================\n")

    def tearDown(self):
        """
        所有测试用例结束之后调用
        """
        BasePage.save_log("===================tearDown===================\n")
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
