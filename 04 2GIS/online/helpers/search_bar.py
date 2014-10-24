from online.helpers.base_component import BaseComponent

class SearchBar(BaseComponent):
    selectors = {
        'self': '.online_searchBar',
        'input': '.searchBar_form.searchBar_textfield._refbook .suggest_input',
        'submit': '.searchBar_submit._refbook'
    }
    def search(self, query):
        self.driver.find_element_by_css_selector(self.selectors['input']).send_keys(query)
        self.driver.find_element_by_css_selector(self.selectors['submit']).submit