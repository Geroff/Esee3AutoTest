# -*- coding: utf-8 -*-

import os
from time import sleep
from enum import Enum
# 此模块需要安装Appium-Python-Client
from appium import webdriver
# 此模块需要安装Pillow
from PIL import Image

# returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

"""
Connection types are specified here:
    https://code.google.com/p/selenium/source/browse/spec-draft.md?repo=mobile#120
    Value (Alias)      | Data | Wifi | Airplane Mode
    -------------------------------------------------
    0 (None)           | 0    | 0    | 0
    1 (Airplane Mode)  | 0    | 0    | 1
    2 (Wifi only)      | 0    | 1    | 0
    4 (Data only)      | 1    | 0    | 0
    6 (All network on) | 1    | 1    | 0
"""


class ConnectionType(Enum):
    NO_CONNECTION = 0
    AIRPLANE_MODE = 1
    WIFI_ONLY = 2
    DATA_ONLY = 4
    ALL_NETWORK_ON = 6


class UiHelper(object):

    def __init__(self, config_path):
        self.desired_caps = {}
        self._driver = None
        self.remoteHost = "http://127.0.0.1:4723/wd/hub"
        # 获取设备配置
        with open(config_path) as file_object:
            for line in file_object:
                if line.startswith("#"):
                    continue

                line = line.strip()
                words = line.split("=")
                if len(words) != 2:
                    continue

                if words[0] == 'app':
                    print(PATH(words[1]))
                    self.desired_caps[words[0]] = PATH(words[1])
                elif words[0] == 'remoteHost':
                    self.remoteHost = words[1]
                else:
                    self.desired_caps[words[0]] = words[1]

    def init_driver(self):
        # 连接服务器
        self._driver = webdriver.Remote(self.remoteHost, self.desired_caps)

    def quit_driver(self):
        # 断开服务器连接
        if self._driver:
            self._driver.quit()

    """
    给定控件的xpatch, id 或者name来查找控件
    
    :Args:
         - element_info: 控件的信息，可以是xpath,id或者其他属性
    
    :Return:
        如果找到控件，返回第一个，否则返回None类型
    
    :Usage:
        self.find_element(element_info)
    """
    def find_element(self, element_info):
        element = None
        if element_info.startswith("//"):
            try:
                element = self._driver.find_element_by_xpath(element_info)
            except:
                pass
        elif ":id/" in element_info or ":string/" in element_info:
            try:
                element = self._driver.find_element_by_id(element_info)
            except:
                pass
        else:
            # 剩下的字符串没有特点，无法区分，因此先尝试通过名称查找
            try:
                element = self._driver.find_element_by_name(element_info)
            except:
                print('by name')
                try:
                    # 如果通过名称不能找到则通过class name查找
                    element = self._driver.find_element_by_class_name(element_info)
                except:
                    pass

        return element

    """
    给定控件的xpatch, id 或者name来查找控件
    
    :Args:
         - element_info: 控件的信息，可以是xpath,id或者其他属性
    
    :Return:
        返回所有满足条件的控件，返回的类型是一个列表，否则返回None类型
    
    :Usage:
        self.find_elements(element_info)
    """
    def find_elements(self, element_info):
        elements = None
        if element_info.startswith("//"):
            try:
                elements = self._driver.find_elements_by_xpath(element_info)
            except:
                pass
        elif ":id/" in element_info:
            try:
                elements = self._driver.find_elements_by_id(element_info)
            except:
                pass
        else:
            try:
                elements = self._driver.find_elements_by_name(element_info)
            except:
                try:
                    elements = self._driver.find_elements_by_class_name(element_info)
                except:
                    pass

        return elements

    """
    在一个已知的控件中通过给定控件的xpatch, id 或者name来查找子控件
    
    :Args:
        - parent_element: 父控件，是一个已知的WebElement
        - child_element_info: 子控件的信息，可以是xpath,id或者其他属性
    
    :Return:
        如果找到控件，返回第一个，否则返回None类型
    
    :Usage:
        self.find_element_in_parent(parent_element, child_element_info)
    """
    def find_element_in_parent(self, parent_element, child_element_info):
        element = None
        if child_element_info.startswith("//"):
            try:
                element = parent_element.find_element_by_xpath(child_element_info)
            except:
                pass
        elif ":id/" in child_element_info:
            try:
                element = parent_element.find_element_by_id(child_element_info)
            except:
                pass
        else:
            try:
                # 剩下的字符串没有特点，无法区分，因此先尝试通过名称查找
                element = parent_element.find_element_by_name(child_element_info)
            except:
                try:
                    # 如果通过名称不能找到则通过class name查找
                    element = parent_element.find_element_by_class_name(child_element_info)
                except:
                    pass

        return element

    """
    在一个已知的控件中通过给定控件的xpatch, id 或者name来查找子控件
    
    :Args:
        - parent_element: 父控件，是一个已知的WebElement
        - child_element_info: 子控件的信息，可以是xpath,id或者其他属性
    
    :Return:
        如果找到控件，返回所有符合条件的控件，否则返回None类型
    
    :Usage:
        self.find_elements_in_parent(parent_element, child_element_info)
    """
    def find_elements_in_parent(self, parent_element, child_element_info):
        elements = None
        if child_element_info.startswith("//"):
            try:
                elements = parent_element.find_elements_by_xpath(child_element_info)
            except:
                pass
        elif ":id/" in child_element_info:
            try:
                elements = parent_element.find_elements_by_id(child_element_info)
            except:
                pass
        else:
            try:
                # 剩下的字符串没有特点，无法区分，因此先尝试通过名称查找
                elements = parent_element.find_elements_by_name(child_element_info)
            except:
                try:
                    # 如果通过名称不能找到则通过class name查找
                    elements = parent_element.find_elements_by_class_name(child_element_info)
                except:
                    pass

        return elements

    """
    通过UIAutomator的uia_string来查找控件
    
    :Args:
        -uia_string: UiSelector相关的代码，参考http://developer.android.com/
        tools/help/uiautomator/UiSelector.html#fromParent%28com.android.uiautomator.core.UiSelector%29
    
    :Return:
        -找到的控件,找不到返回None类型
    
    :Usage:
        self.find_element_by_ui_automator(new UiSelector().(android.widget.LinearLayout))
    """
    def find_element_by_ui_automator(self, uia_string):
        try:
            return self._driver.find_element_by_android_uiautomator(uia_string)
        except:
            return None

    """
    滑动操作
    
    :Args:
         - x1,y1,x2,y2： 滑动操作的起点和终点的坐标
    
    :Usage:
        self.swipe(50, 50, 400, 400)
    """
    def flick(self, x1, y1, x2, y2):
        self._driver.flick(x1, y1, x2, y2)

    """
    滑动操作
    
    :Args:
         - x1,y1,x2,y2： 滑动操作的起点和终点的坐标
         - duration: 多长时间内完成该操作,单位是毫秒
    
    :Usage:
        self.swipe(50, 50, 400, 400, 500)
    """
    def swipe(self, x1, y1, x2, y2, duration):
        self._driver.swipe(x1, y1, x2, y2, duration)

    def tap(self, x, y):
        self._driver.tap([(x, y)])

    """
    长按点击操作
    :Args:
     - x,y： 长按点的坐标
     - duration: 多长时间内完成该操作,单位是毫秒
    
    :Usage:
        self.long_press(50, 50, 500)
    """
    def long_press(self, x, y, duration):
        self._driver.tap([(x, y)], duration)

    """
    点击某一个控件，如果改控件不存在则会抛出异常
    
    :Args:
         - element_info: 控件的信息，可以是xpath,id或者其他属性
    
    :Usage:
        self.click_element(element_info)
    """
    def click_element(self, element_info):
        element = self.find_element(element_info)
        if element is not None:
            print("click")
            element.click()

    """
    获取某个控件显示的文本，如果该控件不能找到则返回None类型
    
    :Args:
         - element_info: 控件的信息，可以是xpath,id或者其他属性
    
    :Return:
        返回该控件显示的文本,否则返回None类型
    
    :Usage:
        self.get_text_of_element(element_info)
        
    """
    def get_text_of_element(self, element_info):
        element = self.find_element(element_info)
        if element is not None:
            return element.text
        return None

    """
     :Args:
     - element_info: 控件的信息，可以是xpath,id或者其他属性
     - message: 要输入的文本
     
     :Usage:
        self.input_text_to_element(element_info, "123")
    """
    def input_text_to_element(self, element_info, message):
        element = self.find_element(element_info)
        if element is not None:
            element.send_keys(message)

    """
    清除文本框里面的文本
    
    :Usage:
        self.clear_text_edit(element_info)
    """
    def clear_text_edit(self, element_info):
        element = self.find_element(element_info)
        if element is not None:
            element.clear()

    """
    按返回键
    
    :Usage:
        self.press_back_key()
    """
    def press_back_key(self):
        # code码参考Android的官网的keycode
        self._driver.press_keycode(4)

    """
    等待某个控件显示
    
    :Args:
         - element_info: 控件的信息，可以是xpath,id或者其他属性
         - duration：等待的秒数
    
    :Usage:
        self.wait_for_element(element_info, 3)
    """
    def wait_for_element(self, element_info, duration):
        for i in range(0, duration):
            sleep(1)
            try:
                element = self.find_element(element_info)
                if element is not None:
                    return True
                continue
            except:
                continue

        return False

    """
    等待某个控件不再显示
    
    :Args:
         - element_info: 控件的信息，可以是xpath,id或者其他属性
         - duration：等待的秒数
    
    :Usage:
        self.wait_for_element_hide(element_info, 3)
    """
    def wait_for_element_hide(self, element_info, duration):
        for i in range(0, duration):
            sleep(1)
            # 不存在了则返回
            if not self.check_element_is_shown(element_info):
                return True
            else:
                continue

        return False

    """
    判断某个控件是否显示
    
    :Args:
         - element_info: 控件的信息，可以是xpath,id或者其他属性
    :Return:
        True: 如果当前画面中期望的控件能被找到
    
    :Usage:
        self.check_element_is_shown(element_info)
    """
    def check_element_is_shown(self, element_info):
        element = self.find_element(element_info)
        return element is not None

    """
    判断某个控件是否显示在另外一个控件中
    
    :Args:
        - parent_element: 父控件，是一个已知的WebElement
        - child_element_info: 子控件的信息，可以是xpath,id或者其他属性
    :Return:
        True: 如果当前画面中期望的控件能被找到
    
    :Usage:
        self.check_element_shown_in_parent(child_element_info)
    """
    def check_element_shown_in_parent(self, parent_element, child_element_info):
        element = self.find_element_in_parent(parent_element, child_element_info)
        return element is not None

    """
    判断某个控件是否被选中
    
    :Args:
         - element_info: 控件的信息，可以是xpath,id或者其他属性
    :Return:
        True: 如果当前画面中期望的控件能被选中
    
    :Usage:
        self.checkElementIsSelected(element_info)
    """
    def check_element_is_selected(self, element_info):
        element = self.find_element(element_info)
        if element is not None:
            return element.is_selected()
        else:
            return False

    """
    判断某个开关控件是否被选中
    
    :Args:
         - element_info: 控件的信息，可以是xpath,id或者其他属性
    :Return:
        True: 如果当前画面中期望的控件能被选中
    
    :Usage:
        self.check_element_is_checked(element_info)
    """
    def check_element_is_checked(self, element_info):
        element = self.find_element(element_info)
        if element is not None:
            if 'false' in element.get_attribute("checked"):
                return False
            else:
                return True
        else:
            return False

    """

    判断某个控件是否enabled，如果不存在则报异常，否则返回'true'或'false'的字符串
    :Args:
         - element_info: 控件的信息，可以是xpath,id或者其他属性
    :Return:
        True: 如果当前画面中期望的控件enabled
    
    :Usage:
        self.check_element_is_enabled(element_info)
    """
    def check_element_is_enabled(self, element_info):
        element = self.find_element(element_info)
        if element is not None:
            return 'true' in element.get_attribute("enabled")
        else:
            return False

    """
      判断某个控件是否checkable，如果不存在则报异常，否则返回'true'或'false'的字符串
      :Args:
           - element_info: 控件的信息，可以是xpath,id或者其他属性
      :Return:
          True: 如果当前画面中期望的控件enabled

      :Usage:
          self.check_element_is_checkable(element_info)
      """

    def check_element_is_checkable(self, element_info):
        element = self.find_element(element_info)
        if element is not None:
            return 'true' in element.get_attribute("checkable")
        else:
            return False

    """
          判断某个控件是否password，如果不存在则报异常，否则返回'true'或'false'的字符串
          :Args:
               - element_info: 控件的信息，可以是xpath,id或者其他属性
          :Return:
              True: 如果当前画面中期望的控件enabled

          :Usage:
              self.check_element_is_password_enable(element_info)
          """

    def check_element_is_password_enable(self, element_info):
        element = self.find_element(element_info)
        if element is not None:
            return 'true' in element.get_attribute("password")
        else:
            return False

    """
    获取当前的Activity
    
    :Return:
        当前Activity的名称,不包括包名，例如：.activity.SplashActivity
    """
    def get_current_activity(self):
        return self._driver.current_activity

    """
    等待某一个Activity显示
    备注：不确定是否适用于ios
    
    :Args:
        -activity_name: 某activity的名称
        -duration: 等待的时间，秒数
    """
    def wait_for_activity(self, activity_name, duration):
        for i in range(0, duration):
            sleep(1)
            try:
                if activity_name in self.get_current_activity():
                    return True
            except:
                continue
        return False

    """
    保存当前手机的屏幕截图到电脑上指定位置
    
    :Args:
         - path_on_pc: 电脑上保存图片的位置
    
    :Usage:
        self.save_screen_shot("c:\test_POI1.jpg")
    """
    def save_screen_shot(self, path_on_pc):
        self._driver.save_screenshot(path_on_pc)
        size = (341, 640)
        try:
            im = Image.open(path_on_pc)
            im.thumbnail(size)
            im.save(path_on_pc, "png")
        except IOError:
            print("cannot create thumbnail for", path_on_pc)

    def set_network(self, net_type):
        pass

    """
    启动测试程序
    """
    def launch_app(self):
        self._driver.launch_app()

    """
    关闭测试程序
    """
    def close_app(self):
        self._driver.close_app()

    """
    获取测试设备的OS
    
    :Return: Android或者ios
    """
    def get_device_os(self):
        return self.desired_caps['platformName']

    """
    只打开wifi连接
    """
    def enable_wifi_only(self):
        if (self._driver.network_connection & 0x2) == 2:
            return
        else:
            self._driver.set_network_connection(ConnectionType.WIFI_ONLY)

    """
    只打开数据连接
    """
    def enable_data_only(self):
        if int(self._driver.network_connection & 4) == 4:
            return
        else:
            self._driver.set_network_connection(ConnectionType.DATA_ONLY)

    """
    获取context
    """
    def get_context(self):
        self._driver.contexts()

    def switch_context(self, context_name):
        self._driver.switch_to.context(context_name)

    """
    打开所有的网络连接
    """
    def enable_all_connection(self):
        self._driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)

    """
    关闭所有网络连接
    """
    def disable_all_connection(self):
        self._driver.set_network_connection(ConnectionType.NO_CONNECTION)

    """
    判断toast信息
    """
    def find_toast(self, message):
        try:
            message = "//*[contains(@text,'%s')]" % message
            element = self.wait_for_element(message, 10)
            return element
        except:
            return False

    """
    获取控件某个像素点的颜色
    
    Args:
        -element_info: 控件的信息，可以是xpath,id或者其他属性
        -x_offset：指定偏移控件起始位置的x坐标值
        -y_offset：指定偏移控件起始位置的y坐标值
    Return:
        颜色值：#ceddf0
    """
    def get_element_color(self, element_info, x_offset=0, y_offset=0):
        element = self.find_element(element_info)
        if element is not None:
            temp_image_file = '..\\main\\report\\temp_color.png'
            # 保存截图
            self._driver.save_screenshot(temp_image_file)
            sleep(1)
            x1 = element.location.get('x')
            y1 = element.location.get('y')
            width = element.size.get('width')
            height = element.size.get('height')
            x2 = x1 + width
            y2 = y1 + height
            if x_offset < 0:
                x_offset = 0

            if x_offset >= (x2 - x1):
                x_offset = x2 - x1

            if y_offset < 0:
                y_offset = 0

            if y_offset >= (y2 - y1):
                y_offset = y2 - y1

            # 打开截图文件
            image = Image.open(temp_image_file)

            # 从截图中裁出控件
            image = image.crop(box=(x1, y1, x2, y2))

            # 如果Alpha不是255，则得考虑转换
            # image = image.convert('RGB')

            # 获取x_offset,y_offset所指定点的像素值
            rgb = image.getpixel((x_offset, y_offset))[0:3]
            color = '#'
            for i in rgb:
                num = str(hex(i)).replace("0x", "")
                color += num
            if os.path.exists(temp_image_file):
                # 移除截图文件
                os.remove(temp_image_file)
            return color
        else:
            return None
