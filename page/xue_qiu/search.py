from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from common.log import Log
from page.base_page import BasePage


class Search(BasePage):
    log = Log()

    def search(func):
        def wrapper(self, *args):
            self.log.info('输入name：{}'.format(*args))
            self.find(MobileBy.ID, 'search_input_text').send_keys(*args)
            func(self, *args)
        return wrapper

    def search_ba(self, name):
        self.find(MobileBy.ID, 'search_input_text').send_keys(name)
        return self._driver.page_source

    @search
    def search_gp(self, name):
        self.log.info('点击股票')
        self.find(By.XPATH, '//*[@text="股票"] and contains(@resource-id, "title_text")]').click()
        return self._driver.page_source

    def search_ht(self, name):
        self.log.info('输入name：{}'.format(name))
        self.find(MobileBy.ID, 'search_input_text').send_keys(*name)
        self.log.info('点击话题')
        self.find(By.XPATH, '//*[@text="话题"] and contains(@resource-id, "title_text")]').click()
        return self._driver.page_source

    def search_yh(self, name):
        self.log.info('输入name：{}'.format(name))
        self.find(MobileBy.ID, 'search_input_text').send_keys(*name)
        self.log.info('点击用户')
        self.find(By.XPATH, '//*[@text="用户"] and contains(@resource-id, "title_text")]').click()
        return self._driver.page_source

    def search_zh(self, name):
        self.log.info('输入name：{}'.format(name))
        self.find(MobileBy.ID, 'search_input_text').send_keys(*name)
        self.log.info('点击组合')
        self.find(By.XPATH, '//*[@text="组合"] and contains(@resource-id, "title_text")]').click()
        return self._driver.page_source

    def add_optional(self, name):
        # 加自选
        self.log.info('输入name：{}'.format(name))
        self.find(MobileBy.ID, 'search_input_text').send_keys(*name)
        self.find(By.XPATH, '//*[@text="阿里巴巴"]').click()
        self.find(By.XPATH, '//*[@text="加自选"]').click()
        self.find(By.XPATH, '//*[@text="下次再说"]').click()
        el = self.find(By.ID, 'follow_btn').text
        return el
