# coding=utf-8

from base import BaseCase
from ui.view import LoginView
from conf.string import StringManager


class LoginTestCase(BaseCase):

    def setUp(self):
        # 调用父类方法
        super(LoginTestCase, self).setUp()
        # 由于第一个启动的是SplashActivity,因此需要等待打开UserLoginActivity界面
        if self.uiHelper.wait_for_activity(LoginView.user_login_activity, 5):
            print(self.uiHelper.get_current_activity())
        else:
            self.uiHelper.quit_driver()
            self.assertFalse("current activity is not login activity")

    def test_user_name_hint_text_is_correct(self):
        """
         测试用户名输入框提示语是否正确
        """
        self.assertEqual(StringManager.user_name_hint_text,
                         self.uiHelper.get_text_of_element(LoginView.login_et_user_name))

    def test_user_password_hint_text_is_correct(self):
        """
        测试密码输入框是否正确
        """
        # 先验证是否是密码模式
        is_password_mode = self.uiHelper.check_element_is_password_enable(LoginView.login_et_user_pwd)
        if is_password_mode:
            # 如果是密码模式，需要点击切换
            self.uiHelper.click_element(LoginView.login_iv_pwd_eye)

        # 密码模式文本为空
        text = self.uiHelper.get_text_of_element(LoginView.login_et_user_pwd)
        print('text-->' + text)
        expected_text = StringManager.user_password_hint_text
        print('expected_text-->' + expected_text)
        self.assertEqual(expected_text, text)

    def test_forget_password_text_is_correct(self):
        """
        测试忘记密码文本是否正确
        """
        self.assertEqual(StringManager.forget_password_text,
                         self.uiHelper.get_text_of_element(LoginView.login_tv_forget_pwd))

    def test_register_text_is_correct(self):
        """
        测试注册文本是否正确
        """
        self.assertEqual(StringManager.register_text,
                         self.uiHelper.get_text_of_element(LoginView.login_tv_register))

    def test_confirm_button_text_is_correct(self):
        """
        测试登录文本是否正确
        """
        self.assertEqual(StringManager.confirm_button_text,
                         self.uiHelper.get_text_of_element(LoginView.login_btn_login))

    def test_user_name_clear_button_display_after_input_data(self):
        """
        测试在用户输入框输入内容后，清除按钮是否显示
        """
        self.uiHelper.input_text_to_element(LoginView.login_et_user_name, "123")
        element = self.uiHelper.find_element(LoginView.login_fl_delete_user)
        self.assertIsNotNone(element)

    def test_pwd_clear_button_display_after_input_data(self):
        """
        测试在密码输入框输入内容后，清除按钮是否显示
        """
        self.uiHelper.input_text_to_element(LoginView.login_et_user_pwd, "123")
        element = self.uiHelper.find_element(LoginView.login_fl_delete_pwd)
        self.assertIsNotNone(element)

    def test_pwd_input_mode(self):
        """
        测试切换密码文本框输入模式
        """
        is_enable = self.uiHelper.check_element_is_password_enable(LoginView.login_et_user_pwd)
        if is_enable:
            self.uiHelper.click_element(LoginView.login_iv_pwd_eye)
        is_enable = self.uiHelper.check_element_is_password_enable(LoginView.login_et_user_pwd)
        self.assertEqual(False, is_enable)

    def test_view_color(self):
        """
        测试控件的背景颜色
        """
        desired_color = '#ceddf0'
        color = self.uiHelper.get_element_color(LoginView.login_btn_login)
        print color
        self.assertEqual(color, desired_color)
