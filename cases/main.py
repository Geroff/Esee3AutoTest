# coding=utf-8

import time
from base import BaseCase
from ui.view import LoginView
from ui.view import MainView


class MainTestCase(BaseCase):

    def setUp(self):
        # 调用父类方法
        super(MainTestCase, self).setUp()
        # 由于第一个启动的是SplashActivity,因此需要等待打开UserLoginActivity界面
        if self.uiHelper.wait_for_activity(LoginView.user_login_activity, 5):
            print(self.uiHelper.get_current_activity())
            # 通过点击体验按钮启动MainActivity,因此需要等待打开MainActivity界面
            self.uiHelper.click_element(LoginView.login_tv_try_one_down)
            if self.uiHelper.wait_for_activity(MainView.user_main_activity, 5):
                print(self.uiHelper.get_current_activity())
            else:
                self.uiHelper.quit_driver()
                self.assertFalse("current activity is not login activity")
        else:
            self.uiHelper.quit_driver()
            self.assertFalse("current activity is not login activity")

    def test_is_device_dialog_show(self):
        """
         测试是否是显示新设备对话框
        """
        time.sleep(2)
        self.assertIsNotNone(self.uiHelper.find_element(MainView.main_device_list_dialog_tv_title))

    def test_sweep(self):
        """
         测试滑动刷新
        """
        time.sleep(2)
        element = self.uiHelper.find_element(MainView.main_device_list_dialog_tv_title)
        if element is not None:
            items = self.uiHelper.find_elements(MainView.main_device_list_dialog_rl_item)
            print(len(items))
            self.uiHelper.press_back_key()
            time.sleep(2)
        self.uiHelper.swipe(400, 400, 400, 800, 100)
        time.sleep(5)




