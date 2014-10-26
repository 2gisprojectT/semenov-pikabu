from pikabu.helpers.basecomponent import BaseComponent

class SearchBar(BaseComponent):

    selectors = {
        'input': '#search_menu',
        'submit': '#serach_block > form > div > input.search_btn'
    }

    def search(self, query):
        self.driver.find_element_by_css_selector(self.selectors['input']).clear()
        self.driver.find_element_by_css_selector(self.selectors['input']).send_keys(query)
        self.driver.find_element_by_css_selector(self.selectors['submit']).submit()