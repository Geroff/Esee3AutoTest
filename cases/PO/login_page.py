# coding=utf-8

from base_page import BasePage


class LoginPage(BasePage):
    page_name = 'UserLoginActivity'

    # 登录界面默认文本
    user_name_hint_text = u'请输入邮箱/手机号'
    user_password_hint_text = u'请输入密码'
    forget_password_text = u'忘记密码？'
    register_text = u'注册'
    confirm_button_text = u'确定'
    login_title_text = u'登录'
    other_login_type_text = u'其他方式登录'
    try_one_down_text = u'体验一下'

    user_name_hint_text_xpath = '//android.widget.EditText[@text="%s"]' % user_name_hint_text
    # 'com.juanvision.eseecloud30:id/user_name_edt'

    # 微信登录授权按钮
    wechat_confirm_login = 'com.tencent.mm:id/bwn'

    # 登录界面标题
    login_title = '%s:id/user_login_title_tv' % BasePage.package_name

    # 用户输入框
    login_et_user_name = '%s:id/user_name_edt' % BasePage.package_name
    # 密码输入框
    login_et_user_pwd = '%s:id/user_pwd_edt' % BasePage.package_name
    # 密码输入模式切换按钮（眼睛）
    login_iv_pwd_eye = '%s:id/password_eye_iv' % BasePage.package_name

    # 用户输入框清除按钮
    login_fl_delete_user = '%s:id/delete_user_fl' % BasePage.package_name
    # 密码输入框清除按钮
    login_fl_delete_pwd = '%s:id/delete_pwd_fl' % BasePage.package_name

    # 忘记密码
    login_tv_forget_pwd = '%s:id/user_login_forget_pwd_tv' % BasePage.package_name
    # 注册
    login_tv_register = '%s:id/user_login_register_tv' % BasePage.package_name

    # 登录确定按钮
    login_btn_login = '%s:id/confirm_btn' % BasePage.package_name
    # 体验一下
    login_tv_try_one_down = '%s:id/try_one_down_tv' % BasePage.package_name

    # 微信登录
    login_iv_wechat = '%s:id/wechat_iv' % BasePage.package_name

    # 其它方式登录
    login_tv_other_login_type = '%s:id/user_login_type_other_login_tv' % BasePage.package_name

    def input_user_name(self, user_name):
        self.ui_helper.input_text_to_element(LoginPage.login_et_user_name, user_name)

    def input_password(self, password):
        self.ui_helper.input_text_to_element(LoginPage.login_et_user_pwd, password)

    def get_user_name(self):
        return self.ui_helper.get_text_of_element(LoginPage.login_et_user_name)

    def get_password(self):
        return self.ui_helper.get_text_of_element(LoginPage.login_et_user_pwd)

    def get_forget_password_text(self):
        return self.ui_helper.get_text_of_element(LoginPage.login_tv_forget_pwd)

    def get_register_text(self):
        return self.ui_helper.get_text_of_element(LoginPage.login_tv_register)

    def get_login_title_text(self):
        return self.ui_helper.get_text_of_element(LoginPage.login_title)

    def get_login_text(self):
        return self.ui_helper.get_text_of_element(LoginPage.login_btn_login)

    def get_other_login_text(self):
        return self.ui_helper.get_text_of_element(LoginPage.login_tv_other_login_type)

    def get_try_one_down_text(self):
        return self.ui_helper.get_text_of_element(LoginPage.login_tv_try_one_down)

    def is_password_mode(self):
        return self.ui_helper.check_element_is_password_enable(LoginPage.login_et_user_pwd)

    def click_password_eye(self):
        self.ui_helper.click_element(LoginPage.login_iv_pwd_eye)

    def click_login_button(self):
        self.ui_helper.click_element(LoginPage.login_btn_login)

    def click_register(self):
        self.ui_helper.click_element(LoginPage.login_tv_register)

    def click_try_one_down(self):
        self.ui_helper.click_element(LoginPage.login_tv_try_one_down)

    def click_wechat(self):
        self.ui_helper.click_element(LoginPage.login_iv_wechat)

    def click_wechat_confirm_login(self):
        self.ui_helper.click_element(LoginPage.wechat_confirm_login)

    def click_delete_user_button(self):
        self.ui_helper.click_element(LoginPage.login_fl_delete_user)

    def click_delete_pwd_button(self):
        self.ui_helper.click_element(LoginPage.login_fl_delete_pwd)

