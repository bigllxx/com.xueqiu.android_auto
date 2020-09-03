import pytest
import yaml

from page.app import App


class TestSearch:
    with open('../data/test_search.data.yaml', encoding='utf8') as f:
        data = yaml.safe_load(f)

    def setup(self):
        self.main = App().start().main()

    @pytest.mark.parametrize('name, exp', data['search'])
    def test_search_gp(self, name, exp):
        res = self.main.goto_xue_qiu().goto_search().search_gp(name)
        assert exp in res
    #
    # def test_search_ht(self, name, exp):
    #     res = self.main.goto_xue_qiu().goto_search().search_ht(name)
    #     assert exp in res
    #
    # def test_search_yh(self, name, exp):
    #     res = self.main.goto_xue_qiu().goto_search().search_yh(name)
    #     assert exp in res
    #
    # def test_search_zh(self, name, exp):
    #     res = self.main.goto_xue_qiu().goto_search().search_zh(name)
    #     assert exp in res
    #
    # def test_add(self):
    #     res = self.main.goto_xue_qiu().goto_search().add_optional('alibaba')
    #     assert "已添加" in res
    #
    #
