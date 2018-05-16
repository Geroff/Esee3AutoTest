# coding=utf-8
from cases.PO.base_page import BasePage


class NotificationPage(BasePage):
    system_mms_package_name = 'com.android.mms'

    notification_dismiss_button = 'com.android.systemui:id/dismiss_btn'

    system_mms_notification_title = 'duoqu_drop_content_title'
    system_mms_notification_text = 'duoqu_drop_content_text'
    system_mms_notification_title_parent = 'duoqu_drop_layout'

    text_view_id_xpath_format = '//android.widget.TextView[@resource-id="%s:id/%s"]'

    notification_verify_title_xpath = text_view_id_xpath_format % (system_mms_package_name,
                                                                   system_mms_notification_title)
    notification_verify_text_xpath = text_view_id_xpath_format % (system_mms_package_name,
                                                                  system_mms_notification_text)
    notification_verify_title_parent_xpath = text_view_id_xpath_format % (system_mms_package_name,
                                                                          system_mms_notification_title_parent)

    verify_code_xpath = '//android.widget.RelativeLayout[@resource-id="%s:id/item_rl"]' % BasePage.package_name

    def drop_down_notification(self):
        self.ui_helper.open_notification()

    def drop_up_notification(self, height):
        print('sweep')
        print(height)
        self.ui_helper.swipe(0, height, 0, 0, 100)

    def wait_for_receive_verify_code(self):
        return self.ui_helper.wait_for_element(NotificationPage.notification_verify_text_xpath, 60)

    def get_verify_text(self):
        return self.ui_helper.get_text_of_element(NotificationPage.notification_verify_text_xpath)

    def test(self):
        web_driver_element = self.ui_helper.find_element(NotificationPage.notification_verify_title_parent_xpath)
        if web_driver_element is not None:
            web_driver_element = self.ui_helper.find_element_in_parent(web_driver_element, NotificationPage.notification_verify_title_xpath)
            print (web_driver_element.text)

    def get_page_height(self):
        web_driver_element = self.ui_helper.find_element('android:id/content')
        if web_driver_element is not None:
            return web_driver_element.rect['height']
        else:
            return 0

    def get_page_width(self):
        web_driver_element = self.ui_helper.find_element('android:id/content')
        if web_driver_element is not None:
            return web_driver_element.rect['width']
        else:
            return 0

