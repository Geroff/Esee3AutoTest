from base_page import BasePage


class MainPage(BasePage):
    page_name = 'MainActivity'

    main_ll_person_info = '%s:id/main_person_info_ll' % BasePage.package_name

    main_ll_person_center = '%s:id/main_person_center_ll' % BasePage.package_name
    main_ll_demo_center = '%s:id/demo_center_ll' % BasePage.package_name
    main_ll_device_center = '%s:id/device_ll' % BasePage.package_name

    def click_person_center(self):
        self.ui_helper.click_element(MainPage.main_ll_person_center)

    def click_person_info(self):
        self.ui_helper.click_element(MainPage.main_ll_person_info)

    def wait_for_person_info_show(self):
        return self.ui_helper.wait_for_element(MainPage.main_ll_person_info, MainPage.time_out)


