# coding=utf-8

from base_page import BasePage
from cases.helper.utils import save_password


class ModifyPasswordPage(BasePage):
    """
    修改密码界面
    """
    page_name = 'ModifyPasswordActivity'

    modify_tv_common_title = '%s:id/common_title_tv' % BasePage.package_name
    modify_et_old_pwd = '%s:id/old_pwd_et' % BasePage.package_name
    modify_et_new_pwd = '%s:id/new_pwd_et' % BasePage.package_name
    modify_et_confirm_pwd = '%s:id/confirm_pwd_et' % BasePage.package_name
    modify_btn_confirm = '%s:id/confirm_btn' % BasePage.package_name

    def input_old_pwd(self, password):
        self.ui_helper.input_text_to_element(ModifyPasswordPage.modify_et_old_pwd, password)

    def input_new_pwd(self, password):
        self.ui_helper.input_text_to_element(ModifyPasswordPage.modify_et_new_pwd, password)

    def input_confirm_pwd(self, password):
        self.ui_helper.input_text_to_element(ModifyPasswordPage.modify_et_confirm_pwd, password)

    def click_confirm_button(self):
        self.ui_helper.click_element(ModifyPasswordPage.modify_btn_confirm)

    def get_title_message(self):
        self.ui_helper.get_text_of_element(ModifyPasswordPage.modify_tv_common_title)

    @staticmethod
    def save_account(password):
        save_password(password)
