# coding=utf-8


import sys
from base_case import BaseCase
from PO.splash_page import SplashPage
from PO.login_page import LoginPage
from ddt import ddt, unpack, data


@ddt
class SplashTestCase(BaseCase):

    def setUp(self):
        # 调用父类方法
        super(SplashTestCase, self).setUp()
        self.splash_page = SplashPage(self.driver)
        if self.splash_page.wait_for_activity(SplashPage.page_name, self.time_out):
            self.is_in_expected_activity = True

    @data((1, False), (4, True))
    @unpack
    def test_wait_go_to_main(self, time_out, expected):
        """
        测试是否等待3秒跳到登录界面
        """
        method_name = sys._getframe().f_code.co_name
        SplashPage.save_log(LogString.is_in_splash_activity % (method_name + '_time_out_' + str(time_out) + '_'
                                                               + str(expected), str(self.is_in_expected_activity)))
        self.assertEqual(True, self.is_in_expected_activity)

        is_in_login_page = self.splash_page.wait_for_activity(LoginPage.page_name, time_out)
        SplashPage.save_log(LogString.is_skip_to_splash_activity % is_in_login_page)
        self.assertEqual(expected, is_in_login_page)

    def test_click_skip(self):
        """
        测试点击跳过按钮, 闪屏页存在不显示跳过按钮
        """
        method_name = sys._getframe().f_code.co_name
        SplashPage.save_log(LogString.is_in_splash_activity % (method_name, self.is_in_expected_activity))
        self.assertEqual(True, self.is_in_expected_activity)

        # 如果不存在跳过按钮，则默认为通过
        is_skip_show = self.splash_page.wait_for_skip_show()
        SplashPage.save_log(LogString.is_show_skip_button % is_skip_show)
        if self.splash_page.wait_for_skip_show():
            self.splash_page.click_skip()
            is_in_login_page = self.splash_page.wait_for_activity(LoginPage.page_name, 1)
            SplashPage.save_log(LogString.is_skip_to_splash_activity % is_in_login_page)
            self.assertEqual(True, is_in_login_page)


class LogString(object):
    """
    日志显示内容，需要在字符串前添加u，否则在拼接时内容时会报错
    """
    is_in_splash_activity = u'测试%s时，是否在闪屏页？-->%s\n'
    is_skip_to_splash_activity = u'是否跳转到登录界面？-->%s\n'
    is_show_skip_button = u'是否显示跳过按钮？-->%s\n'
