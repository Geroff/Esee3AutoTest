# coding=utf-8

from base_page import BasePage


class ModifyPasswordDialogPage(BasePage):
    """
    修改密码界面中的对话框
    """

    modify_tv_dialog_content = '%s:id/dialog_content_tv' % BasePage.package_name
    modify_tv_dialog_confirm = '%s:id/dialog_confirm_btn' % BasePage.package_name

    content_text = '密码修改成功，下次登录生效'
    confirm_button_text = '确定'

    content_xpath = '//android.widget.TextView[@text="%s"]' % content_text
    confirm_button_xpath = '//android.widget.Button[@text="%s"]' % confirm_button_text

    def click_confirm_button(self):
        self.ui_helper.click_element(ModifyPasswordDialogPage.modify_tv_dialog_confirm)

    def get_dialog_content(self):
        return self.ui_helper.get_text_of_element(ModifyPasswordDialogPage.modify_tv_dialog_content)

    def wait_for_confirm_show(self):
        return self.ui_helper.wait_for_element(ModifyPasswordDialogPage.modify_tv_dialog_confirm,
                                               ModifyPasswordDialogPage.time_out)

