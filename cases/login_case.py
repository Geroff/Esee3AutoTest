# coding=utf-8

import sys
from base_case import BaseCase
from PO.login_page import LoginPage
from PO.main_page import MainPage
from PO.splash_page import SplashPage
from PO.new_device_dialog_page import NewDeviceDialogPage
from PO.register_page import RegisterPage
from ddt import ddt, data, unpack
from cases.helper.utils import get_account

# 获取账号密码
account = get_account()
valid_account = account['valid_count']
valid_phone_account = valid_account['account']
valid_phone_password = valid_account['password']

invalid_phone_password = valid_phone_password[::-1]
print(valid_phone_account + ' ' + valid_phone_password + ' ' + invalid_phone_password)


@ddt
class LoginTestCase(BaseCase):
    """
    测试登录界面
    """

    def setUp(self):
        # 调用父类方法
        super(LoginTestCase, self).setUp()
        self.login_page = LoginPage(self.driver)

        if self.login_page.wait_for_activity(SplashPage.page_name, self.time_out):
            if self.login_page.wait_for_element(SplashPage.splash_tv_skip, self.time_out):
                SplashPage(self.driver).click_skip()

        if self.login_page.wait_for_activity(LoginPage.page_name, self.time_out):
            self.is_in_expected_page = True

    def test_default_user_name_is_correct(self):
        """
        测试默认用户名提示是否正确
        """
        method_name = sys._getframe().f_code.co_name
        LoginPage.save_log(LogString.is_in_login_page % (method_name, self.is_in_expected_page))
        self.assertEqual(True, self.is_in_expected_page)

        user_name = self.login_page.get_user_name()
        LoginPage.save_log(LogString.current_user_name % user_name)
        self.assertEqual(LoginPage.user_name_hint_text, user_name)

    def test_default_password_is_correct(self):
        """
        测试默认密码框提示是否正确
        """
        method_name = sys._getframe().f_code.co_name
        LoginPage.save_log(LogString.is_in_login_page % (method_name, self.is_in_expected_page))
        self.assertEqual(True, self.is_in_expected_page)

        # 先验证是否是密码模式
        is_password_mode = self.login_page.is_password_mode()
        LoginPage.save_log(LogString.is_password_mode % is_password_mode)
        if is_password_mode:
            # 如果是密码模式，需要点击切换
            self.login_page.click_password_eye()
            LoginPage.save_log(LogString.click_pwd_eye_to_change_mode)
        password = self.login_page.get_password()
        LoginPage.save_log(LogString.current_password % password)
        self.assertEqual(LoginPage.user_password_hint_text, password)

    def test_forget_password_text_is_correct(self):
        """
        测试忘记密码文本是否正确
        """
        method_name = sys._getframe().f_code.co_name
        LoginPage.save_log(LogString.is_in_login_page % (method_name, self.is_in_expected_page))
        self.assertEqual(True, self.is_in_expected_page)

        forget_password_text = self.login_page.get_forget_password_text()
        LoginPage.save_log(LogString.forget_password_text % forget_password_text)
        self.assertEqual(LoginPage.forget_password_text,
                         forget_password_text)

    def test_register_text_is_correct(self):
        """
        测试注册文本是否正确
        """
        method_name = sys._getframe().f_code.co_name
        LoginPage.save_log(LogString.is_in_login_page % (method_name, self.is_in_expected_page))
        self.assertEqual(True, self.is_in_expected_page)

        register_text = self.login_page.get_register_text()
        LoginPage.save_log(LogString.register_text % register_text)
        self.assertEqual(LoginPage.register_text,
                         register_text)

    def test_try_one_down_is_correct(self):
        """
        测试体验一下文本是否正确
        """
        method_name = sys._getframe().f_code.co_name
        LoginPage.save_log(LogString.is_in_login_page % (method_name, self.is_in_expected_page))
        self.assertEqual(True, self.is_in_expected_page)

        try_one_down_text = self.login_page.get_try_one_down_text()
        LoginPage.save_log(LogString.try_one_down_text % try_one_down_text)
        self.assertEqual(LoginPage.try_one_down_text,
                         try_one_down_text)

    def test_login_text_is_correct(self):
        """
        测试登录文本是否正确
        """
        method_name = sys._getframe().f_code.co_name
        LoginPage.save_log(LogString.is_in_login_page % (method_name, self.is_in_expected_page))
        self.assertEqual(True, self.is_in_expected_page)

        login_title_text = self.login_page.get_login_title_text()
        LoginPage.save_log(LogString.login_title_text % login_title_text)
        self.assertEqual(LoginPage.login_title_text,
                         login_title_text)

    def test_login_title_text_is_correct(self):
        """
        测试登录标题文本是否正确
        """
        method_name = sys._getframe().f_code.co_name
        LoginPage.save_log(LogString.is_in_login_page % (method_name, self.is_in_expected_page))
        self.assertEqual(True, self.is_in_expected_page)

        login_text = self.login_page.get_login_text()
        LoginPage.save_log(LogString.try_one_down_text % login_text)
        self.assertEqual(LoginPage.confirm_button_text,
                         login_text)

    def test_other_login_text_is_correct(self):
        """
        测试其他方式登录文本是否正确
        """
        method_name = sys._getframe().f_code.co_name
        LoginPage.save_log(LogString.is_in_login_page % (method_name, self.is_in_expected_page))
        self.assertEqual(True, self.is_in_expected_page)

        other_login_type = self.login_page.get_other_login_text()
        LoginPage.save_log(LogString.other_login_text % other_login_type)
        self.assertEqual(LoginPage.other_login_type_text,
                         other_login_type)

    @data(
        (valid_phone_account, valid_phone_password, True),
        (valid_phone_account, invalid_phone_password, False)
    )
    @unpack
    def test_login(self, user_name, password, expected_result):
        """
        测试用户登录
        :param user_name: 用户名
        :param password: 密码
        :param expected_result: 预期结果
        """
        method_name = sys._getframe().f_code.co_name
        method_name = method_name + '_' + user_name + '_' + password + '_' + str(expected_result)

        LoginPage.save_log(LogString.is_in_login_page % (method_name, self.is_in_expected_page))
        if not self.is_in_expected_page:
            self.login_page.save_screen_shot(method_name)

        self.assertEqual(True, self.is_in_expected_page)

        self.login_page.input_user_name(user_name)
        self.login_page.input_password(password)
        LoginPage.save_log(LogString.current_user_name % user_name + '\n' + LogString.current_password % password)
        self.login_page.click_login_button()

        new_device_dialog_page = NewDeviceDialogPage(self.driver)
        is_in_main_page = new_device_dialog_page.wait_for_dialog_show()
        if not is_in_main_page:
            is_in_main_page = self.login_page.wait_for_activity(MainPage.page_name, self.time_out)

        LoginPage.save_log(LogString.is_in_main_page % is_in_main_page)
        self.login_page.save_screen_shot(method_name)
        self.assertEqual(expected_result, is_in_main_page)

    def test_wechat_login(self):
        """
        测试微信登录功能
        """
        method_name = sys._getframe().f_code.co_name
        LoginPage.save_log(LogString.is_in_login_page % (method_name, self.is_in_expected_page))
        self.assertEqual(True, self.is_in_expected_page)

        self.login_page.click_wechat()

        # 如果已经授权的话，点击微信登录会直接跳转到主界面，所以这里先验证是否跳转到主界面
        # 可能会弹出新设备对话框，所以需要先检测是否是新设备对话框，如果复杂些还会出现其他的对话框，比如权限等
        new_device_dialog_page = NewDeviceDialogPage(self.driver)
        is_in_main_page = new_device_dialog_page.wait_for_dialog_show()
        if not is_in_main_page:
            is_in_main_page = self.login_page.wait_for_activity(LoginPage.page_name, self.time_out)
        LoginPage.save_log(LogString.is_in_main_page_after_click_wechat_button % self.is_main_activity)
        # 如果不是主界面，则判断是否是微信授权登录界面
        if not is_in_main_page:
            is_wechat_confirm_login_show = self.login_page.wait_for_element(LoginPage.wechat_confirm_login, self.time_out)
            self.assertEqual(True, is_wechat_confirm_login_show)

            self.login_page.click_wechat_confirm_login()
            is_in_main_page = new_device_dialog_page.wait_for_dialog_show()
            if not is_in_main_page:
                is_in_main_page = self.login_page.wait_for_activity(LoginPage.page_name, self.time_out)
            LoginPage.save_log(LogString.is_in_main_page_after_click_wechat_authorized_button % self.is_main_activity)
            self.assertEqual(True, is_in_main_page)

    def test_go_to_register(self):
        """
        测试跳转到注册界面
        """
        method_name = sys._getframe().f_code.co_name
        LoginPage.save_log(LogString.is_in_login_page % (method_name, self.is_in_expected_page))
        self.assertEqual(True, self.is_in_expected_page)

        self.login_page.click_register()
        is_register_activity = self.login_page.wait_for_activity(RegisterPage.page_name, self.time_out)
        LoginPage.save_log(LogString.is_in_register_page % self.is_register_activity)
        self.assertEqual(True, is_register_activity)

    # def test_user_name_clear_button_display_after_input_data(self):
    #     """
    #     测试在用户输入框输入内容后，清除按钮是否显示
    #     """
    #     self.login_page.input_text_to_element(LoginPage.login_et_user_name, "123")
    #     element = self.login_page.find_element(LoginPage.login_fl_delete_user)
    #     self.assertIsNotNone(element)

    # def test_pwd_clear_button_display_after_input_data(self):
    #     """
    #     测试在密码输入框输入内容后，清除按钮是否显示
    #     """
    #     self.login_page.input_text_to_element(LoginPage.login_et_user_pwd, "123")
    #     element = self.login_page.find_element(LoginPage.login_fl_delete_pwd)
    #     self.assertIsNotNone(element)

    # def test_pwd_input_mode(self):
    #     """
    #     测试切换密码文本框输入模式
    #     """
    #     is_enable = self.login_page.check_element_is_password_enable(LoginPage.login_et_user_pwd)
    #     if is_enable:
    #         self.login_page.click_element(LoginPage.login_iv_pwd_eye)
    #     is_enable = self.login_page.check_element_is_password_enable(LoginPage.login_et_user_pwd)
    #     self.assertEqual(False, is_enable)

    # def test_view_color(self):
    #     """
    #     测试控件的背景颜色
    #     """
    #     desired_color = '#ceddf0'
    #     color = self.login_page.get_element_color(LoginPage.login_btn_login)
    #     # self.login_page.save_screen_shot('..\\main\\report\\test_view_color.png')
    #     print color
    #     self.assertEqual(color, desired_color)


class LogString(object):
    """
    日志显示内容，需要在字符串前添加u
    """
    is_in_login_page = u'测试%s时，是否在登录界面？-->%s\n'
    is_in_main_page = u'是否在主界面？-->%s\n'
    is_in_register_page = u'是否在注册界面？-->%s\n'
    is_password_mode = u'密码输入框是否是密码模式？-->%s\n'
    click_pwd_eye_to_change_mode = u'点击密码右侧的眼睛，切换密码显示模式'
    current_user_name = u'当前用户名内容为-->%s\n'
    current_password = u'当前密码内容为-->%s\n'
    forget_password_text = u'忘记密码显示的内容为-->%s\n'
    register_text = u'注册显示的文本为-->%s\n'
    try_one_down_text = u'体验一下显示的文本为-->%s\n'
    login_button_text = u'登录按钮显示的文本为-->%s\n'
    login_title_text = u'登录标题显示的文本为-->%s\n'
    other_login_text = u'其他方式登录显示的文本为-->%s\n'
    is_in_main_page_after_click_wechat_button = u'点击微信登录后是否直接跳转到主界面？-->%s\n'
    is_in_main_page_after_click_wechat_authorized_button = u'点击微信授权登录按钮后是否直接跳转到主界面？-->%s\n'
