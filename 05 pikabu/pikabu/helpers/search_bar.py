from pikabu.helpers.basecomponent import BaseComponent

class SearchBar(BaseComponent):

    selectors = {
        'input': '#search_menu',
        'submit': '#serach_block > form > div > input.search_btn',
        'count_results': '#wrap > table > tbody > tr > td.main > table:nth-child(1) > tbody > tr > td:nth-child(2) > div > div > div'
    }

    def search(self, query):
        self.driver.find_element_by_css_selector(self.selectors['input']).clear()
        self.driver.find_element_by_css_selector(self.selectors['input']).send_keys(query)
        self.driver.find_element_by_css_selector(self.selectors['submit']).submit()

    @property
    def count_results(self):
        return self.driver.find_element_by_css_selector(self.selectors['count_results']).text