from base_page import BasePage


class PersonInfoPage(BasePage):
    page_name = 'PersonalInformationActivity'

    main_ll_modify_password = '%s:id/modify_password_ll' % BasePage.package_name

    def click_modify_password(self):
        self.ui_helper.click_element(PersonInfoPage.main_ll_modify_password)
