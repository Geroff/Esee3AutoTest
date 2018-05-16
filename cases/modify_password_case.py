# coding=utf-8
import sys
from base_case import BaseCase
from PO.modify_password_page import ModifyPasswordPage
from PO.splash_page import SplashPage
from PO.login_page import LoginPage
from PO.main_page import MainPage
from PO.new_device_dialog_page import NewDeviceDialogPage
from PO.modify_password_dialog_page import ModifyPasswordDialogPage
from PO.person_info_page import PersonInfoPage

from cases.helper.utils import get_account
from ddt import ddt, unpack, data

# 获取账号密码
account = get_account()
valid_account = account['valid_count']
valid_phone_account = valid_account['account']
old_phone_password = valid_account['password']
new_phone_password = old_phone_password[::-1]
print(old_phone_password + ' ' + new_phone_password)


@ddt
class ModifyPasswordTestCase(BaseCase):

    def setUp(self):
        # 调用父类方法
        super(ModifyPasswordTestCase, self).setUp()
        self.modify_password_page = ModifyPasswordPage(self.driver)
        if self.modify_password_page.wait_for_activity(SplashPage.page_name, self.time_out):
            splash_page = SplashPage(self.driver)
            if splash_page.wait_for_skip_show():
                splash_page.click_skip()
                if self.modify_password_page.wait_for_activity(LoginPage.page_name, self.time_out):
                    login_page = LoginPage(self.driver)
                    login_page.input_user_name(valid_phone_account)
                    login_page.input_password(old_phone_password)
                    login_page.click_login_button()

                new_device_dialog_page = NewDeviceDialogPage(self.driver)
                # 先检测是否显示新设备对话框
                if new_device_dialog_page.wait_for_dialog_show():
                    new_device_dialog_page.back_press()

                if self.modify_password_page.wait_for_activity(MainPage.page_name, self.time_out):
                    main_page = MainPage(self.driver)
                    main_page.click_person_center()

                    if main_page.wait_for_person_info_show():
                        main_page.click_person_info()

                    if self.modify_password_page.wait_for_activity(PersonInfoPage.page_name, self.time_out):
                        PersonInfoPage(self.driver).click_modify_password()

                        if self.modify_password_page.wait_for_activity(ModifyPasswordPage.page_name, self.time_out):
                            self.is_in_expected_activity = True

    @data((old_phone_password, new_phone_password, new_phone_password, True))
    @unpack
    def test_modify_password(self, old_password, new_password, new_password_confirm, expected):
        method_name = sys._getframe().f_code.co_name
        ModifyPasswordPage.save_log(
            LogString.is_in_modify_password_page % (method_name + '_old_' + str(new_password) + '_new_' + str(
                new_password) + '_' + new_password_confirm + '_' + str(expected), self.is_in_expected_activity))
        self.modify_password_page.save_screen_shot(method_name)
        self.assertEqual(True, self.is_in_expected_activity)

        self.modify_password_page.input_old_pwd(old_password)
        self.modify_password_page.input_new_pwd(new_password)
        self.modify_password_page.input_confirm_pwd(new_password_confirm)
        self.modify_password_page.click_confirm_button()

        modify_password_dialog_page = ModifyPasswordDialogPage(self.driver)
        is_confirm_dialog_show = modify_password_dialog_page.wait_for_confirm_show()
        ModifyPasswordPage.save_log(LogString.is_confirm_dialog_show % (old_password, new_password, new_password_confirm, str(is_confirm_dialog_show)))
        self.modify_password_page.save_screen_shot(method_name)
        self.assertEqual(True, is_confirm_dialog_show)
        modify_password_dialog_page.click_confirm_button()

        is_in_login_activity = self.modify_password_page.wait_for_activity(LoginPage.page_name, self.time_out)
        self.modify_password_page.save_account(new_password)
        self.modify_password_page.save_screen_shot(method_name+'_should_go_to_login')
        ModifyPasswordPage.save_log(LogString.is_in_login_page_after_click_confirm_button % str(is_in_login_activity))
        self.assertEqual(expected, is_in_login_activity)


class LogString(object):
    """
       日志显示内容，需要在字符串前添加u,表示unicode编码
    """
    is_in_modify_password_page = u'测试%s时，是否在修改密码界面？-->%s\n'
    is_confirm_dialog_show = u'输入正确的原始密码%s,正确的新密码第一次%s,第二次%s，是否显示确定按钮？-->%s\n'
    is_in_login_page_after_click_confirm_button = u'点击确定按钮后，是否回到登录界面？-->%s\n'
