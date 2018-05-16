# coding=utf-8

import time
from base_case import BaseCase
from PO.notification_page import NotificationPage

class MainTestCase(BaseCase):

    def setUp(self):
        # 调用父类方法
        super(MainTestCase, self).setUp()

    # def test_is_device_dialog_show(self):
    #     """
    #      测试是否是显示新设备对话框
    #     """
    #     time.sleep(2)
    #     self.assertIsNotNone(self.uiHelper.find_element(MainView.main_device_list_dialog_tv_title))
    #
    # def test_sweep(self):
    #     """
    #      测试滑动刷新
    #     """
    #     time.sleep(2)
    #     element = self.uiHelper.find_element(MainView.main_device_list_dialog_tv_title)
    #     if element is not None:
    #         items = self.uiHelper.find_elements(MainView.main_device_list_dialog_rl_item)
    #         print(len(items))
    #         self.uiHelper.press_back_key()
    #         time.sleep(2)
    #     self.uiHelper.swipe(400, 400, 400, 800, 100)
    #     time.sleep(5)

    def test_drop_down_notification(self):
        time.sleep(5)
        notification_page = NotificationPage(self.driver)
        height = notification_page.get_page_height() - 10  # 需要小于屏幕高度，否则会报错
        notification_page.drop_down_notification()
        time.sleep(5)
        # is_receive_verify_code = notification_page.wait_for_receive_verify_code()
        # print ('is_receive_verify_code?' + str(is_receive_verify_code))
        # notification_page.get_verify_text()
        # notification_page.test()

        notification_page.drop_up_notification(height)
        time.sleep(5)





