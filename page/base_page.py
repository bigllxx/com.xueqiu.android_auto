import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
import logging


class BasePage:
    logging.basicConfig(level=logging.INFO)
    _driver: WebDriver
    _black_list = [  # 黑名单，升级弹框等
        (By.ID, 'tv_agree'),
        (By.XPATH, '//*[@text="确定"]'),
        (By.ID, 'image_cancel'),
        (By.XPATH, '//*[@text="下次再说"]')
    ]
    _error_max = 10
    _error_count = 0
    _params = {}

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, by, locator: str = None):
        """
        封装定位方法，及升级、评价、服务协议弹框等处理
        :param by:
        :param locator:
        :return:
        """
        try:
            # 寻找控件
            element = self._driver.find_element(*by) if isinstance(by, tuple) else self._driver.find_element(by, locator)
            # 如果成功，清空错误计数
            self._error_count = 0
            return element
        # done:   self._error_count = 0
        except Exception as e:
            # 如果次数太多，就退出异常逻辑，直接报错
            if self._error_count > self._error_max:
                raise e
            # 记录一直异常的次数
            self._error_count += 1
            # 对黑名单里的弹框进行处理
            for element in self._black_list:
                logging.info(element)
                elements = self._driver.find_elements(*element)
                if len(elements) > 0:
                    elements[0].click()
                    # 继续寻找原来的正常控件
                    return self.find(by, locator)
            # 如果黑名单也没有，就报错
            logging.warning("black list no one found")
            raise e

    def steps(self, path):
        """
        数据驱动，yaml文件读取、替换和操作
        :param path:
        :return:
        """
        with open(path) as f:
            steps: list = yaml.safe_load(f)
            
            element: WebElement
            for step in steps:
                logging.info(step)
                if "by" in step.keys():
                    element = self.find(step["by"], step["locator"])
                if "action" in step.keys():
                    action = step["action"]
                    if action == "find":
                        pass
                    elif action == "click":
                        element.click()
                    elif action == "text":
                        element.text()
                    elif action == "attribute":
                        element.get_attribute(step["value"])
                    elif action in ["send", "input"]:
                        content: str = step["value"]
                        for key in self._params.keys():
                            content = content.replace("{%s}" % key, self._params[key])
                        element.send_keys(content)
