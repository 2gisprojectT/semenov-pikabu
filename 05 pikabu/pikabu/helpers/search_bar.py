from pikabu.helpers.basecomponent import BaseComponent

class SearchBar(BaseComponent):

    selectors = {
        'input': '#search_menu',
        'submit': '#serach_block > form > div > input.search_btn',
        'count_results': '#wrap > table > tbody > tr > td.main > table:nth-child(1) > tbody > tr > td:nth-child(2) > div > div > div',
        'search_string': '#news_search',
        'no_result': '#wrap > table > tbody > tr > td.main > table:nth-child(1) > tbody > tr > td:nth-child(2) > div > div:nth-child(2)'
    }

    def search(self, query):
        self.driver.get("http://pikabu.ru")
        self.driver.find_element_by_css_selector(self.selectors['input']).clear()
        self.driver.find_element_by_css_selector(self.selectors['input']).send_keys(query)
        self.driver.find_element_by_css_selector(self.selectors['submit']).submit()

    @property
    def count_results(self):
        try:
            return int((self.driver.find_element_by_css_selector(self.selectors['count_results']).text)[9:])
        except Exception:
            return 0

    @property
    def search_string(self):
        return self.driver.find_element_by_css_selector(self.selectors['search_string']).get_attribute("value")

    @property
    def search_noresult(self):
        try:
            return self.driver.find_element_by_css_selector(self.selectors['no_result']).text
        except Exception:
            return "False"