from selenium.webdriver.common.by import By
from common.log import Log
from page.base_page import BasePage
from page.deal.index import DealIndex
from page.market.index import MarketIndex
from page.my_self.index import MySelfIndex
from page.xue_qiu.index import XueQiuIndex


class Index(BasePage):
    """
    登陆后的首页，负责将driver分发给4个一级菜单（deal，market，my_self，xue_qiu）
    """
    log = Log()

    def goto_xue_qiu(self):
        self.log.info('分发driver给一级菜单雪球')
        return XueQiuIndex(self._driver)

    def goto_market(self):
        self.log.info('点击行情')
        self.find(By.XPATH, '//*[@test="行情"]').click()
        self.log.info('分发driver给一级菜单行情')
        return MarketIndex(self._driver)

    def goto_deal(self):
        self.log.info('点击交易')
        self.find(By.XPATH, '//*[@test="交易"]').click()
        self.log.info('分发driver给一级菜单交易')
        return DealIndex(self._driver)

    def goto_myself(self):
        self.log.info('点击我的')
        self.find(By.XPATH, '//*[@test="我的"]').click()
        self.log.info('分发driver给一级菜单我的')
        return MySelfIndex(self._driver)
