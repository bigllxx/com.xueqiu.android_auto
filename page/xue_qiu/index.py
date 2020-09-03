from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from page.xue_qiu.attention import Attention
from page.xue_qiu.live_day import LiveDay
from page.xue_qiu.search import Search
from common.log import Log


class XueQiuIndex(BasePage):
    """
    接收首页driver的一级菜单，传递driver给二级菜单或功能集(attention.py,live_day.py,posted.py,search.py)
    """
    log = Log()

    def goto_search(self) -> Search:
        self.log.info('点击搜索输入框')
        self.find(MobileBy.ID, 'home_search').click()
        self.log.info('传递driver给Search类')
        return Search(self._driver)

    def goto_attention(self):
        self.log.info('点击关注')
        self.find(By.XPATH, '//*[@text="关注" and contains(@resource-id, "title_text")]').click()
        self.log.info('传递driver给Attention类')
        return Attention(self._driver)

    def goto_live_day(self):
        self.log.info('点击领红包')
        self._driver.find_elements_by_class_name('android.widget.FrameLayout')[4].click()
        self.log.info('传递driver给LiveDay类')
        return LiveDay(self._driver)

