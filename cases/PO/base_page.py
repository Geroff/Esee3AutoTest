# coding=utf-8

from cases.helper.ui_helper import UiHelper
from cases.helper import utils


class BasePage(object):
    package_name = 'com.juanvision.eseecloud30'

    # 超时时间
    time_out = 10

    def __init__(self, driver):
        self.ui_helper = UiHelper(driver)

    def wait_for_activity(self, activity, timeout):
        return self.ui_helper.wait_for_activity(activity, timeout)

    def wait_for_element(self, element_info, timeout):
        return self.ui_helper.wait_for_element(element_info, timeout)

    def get_current_activity(self):
        return self.ui_helper.get_current_activity()

    def save_screen_shot(self, name):
        return self.ui_helper.save_screen_shot(utils.save_png_name(name))

    def get_current_network(self):
        return self.ui_helper.get_current_network()

    def back_press(self):
        self.ui_helper.press_back_key()

    @staticmethod
    def save_log(message):
        utils.save_log(message)

    def quit_driver(self):
        self.ui_helper.quit_driver()






