# coding=utf-8
from base_page import BasePage


class NewDeviceDialogPage(BasePage):
    """
    新设备对话框界面
    """
    new_device_title = '新设备'
    title_xpath = '//android.widget.TextView[@text="%s"]' % new_device_title

    device_list_xpath = '//android.widget.RelativeLayout[@resource-id="%s:id/item_rl"]' % BasePage.package_name
    # device_xpath = '(//android.widget.RelativeLayout[@resource-id="%s:id/item_rl"])' % BasePage.package_name

    def get_device_list(self):
        self.ui_helper.find_elements(NewDeviceDialogPage.device_list_xpath)

    def click_device(self, index):
        device_xpath = '(%s)[%s]' % (NewDeviceDialogPage.device_list_xpath, index)
        self.ui_helper.click_element(device_xpath)

    def is_title_show(self):
        title_element = self.ui_helper.find_element(NewDeviceDialogPage.title_xpath)
        if title_element is not None:
            return True
        else:
            return False

    def wait_for_dialog_show(self):
        return self.ui_helper.wait_for_element(NewDeviceDialogPage.title_xpath, 5)
