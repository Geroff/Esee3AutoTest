from base_page import BasePage


class SplashPage(BasePage):
    page_name = 'SplashActivity'

    splash_tv_skip = '%s:id/skip_tv' % BasePage.package_name

    def click_skip(self):
        self.ui_helper.click_element(SplashPage.splash_tv_skip)

    def wait_for_skip_show(self):
        return self.ui_helper.wait_for_element(SplashPage.splash_tv_skip, 3)
