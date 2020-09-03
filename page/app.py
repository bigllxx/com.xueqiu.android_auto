import datetime
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from page.base_page import BasePage
from page.index import Index
from common.log import Log


class App(BasePage):
    """
    启动被测app进程
    """
    _package = "com.xueqiu.android"
    _activity = ".view.WelcomeActivityAlias"
    log = Log()

    def start(self):
        if self._driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "192.168.137.3:5555"
            caps["appPackage"] = self._package
            caps["appActivity"] = self._activity
            caps["noReset"] = True  # 不清除数据
            # caps["dontStopAppOnReset"] = True  # 不杀死进程，从当前界面开始执行
            # caps["unicodeKeyboard"] = True # 编码，输入中文时需要
            # caps["resetKeyboard"] = True  # 重置键盘，默认不重置
            # caps["skipServerInstallation"] = True  # 提高性能的
            # caps["chromedriverExecutableDir"]="/Users/seveniruby/projects/chromedriver/all"
            # caps["chromedriverExecutable"] = "D:/android/driver/78.0.3904.11/chromedriver.exe"  # 指定chromedriver,webview调试时需要

            # caps['avd'] = 'Pixel_2_API_23'

            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.log.info('打开app')
            self._driver.implicitly_wait(5)
        else:
            self._driver.start_activity(self._package, self._activity)
            self.log.info('复用driver')
        return self

    def restart(self):
        pass

    def main(self) -> Index:

        def wait_load(driver):
            source = self._driver.page_source
            if "我的" in source:
                return True
            if "同意" in source:
                return True
            if "image_cancel" in source:
                return True
            return False

        WebDriverWait(self._driver, 30).until(wait_load)  # 等待wait_load()为True
        self.log.info('进入首页成功')
        return Index(self._driver)
