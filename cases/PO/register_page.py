from base_page import BasePage


class RegisterPage(BasePage):
    page_name = 'RegisterActivity'

    register_et_user_name = '%s:id/user_name_edt' % BasePage.package_name

    register_btn_confirm = '%s:id/confirm_btn' % BasePage.package_name
    register_tv_title = '%s:id/title_tv' % BasePage.package_name
    register_tv_new_login = '%s:id/new_login_tv' % BasePage.package_name

    register_iv_user_protocol = '%s:id/user_protocol_iv' % BasePage.package_name
    register_tv_user_protocol = '%s:id/user_protocol_tv' % BasePage.package_name

    register_fl_back = '%s:id/back_fl' % BasePage.package_name

    def input_user_name(self, user_name):
        self.ui_helper.input_text_to_element(RegisterPage.register_et_user_name, user_name)

