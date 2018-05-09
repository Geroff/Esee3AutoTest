class BaseView(object):
    package_name = 'com.juanvision.eseecloud30'


class LoginView(BaseView):
    user_login_activity = 'UserLoginActivity'

    login_et_user_name = '%s:id/user_name_edt' % BaseView.package_name
    login_et_user_pwd = '%s:id/user_pwd_edt' % BaseView.package_name
    login_iv_pwd_eye = '%s:id/password_eye_iv' % BaseView.package_name
    login_fl_delete_user = '%s:id/delete_user_fl' % BaseView.package_name
    login_fl_delete_pwd = '%s:id/delete_pwd_fl' % BaseView.package_name
    login_tv_forget_pwd = '%s:id/user_login_forget_pwd_tv' % BaseView.package_name
    login_tv_register = '%s:id/user_login_register_tv' % BaseView.package_name
    login_btn_login = '%s:id/confirm_btn' % BaseView.package_name
    login_tv_try_one_down = '%s:id/try_one_down_tv' % BaseView.package_name


class MainView(BaseView):
    user_main_activity = 'MainActivity'

    main_device_list_dialog_tv_title = '%s:id/title_tv' % BaseView.package_name
    main_device_list_dialog_rl_item ='%s:id/item_rl' % BaseView.package_name
