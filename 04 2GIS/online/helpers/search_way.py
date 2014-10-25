from online.helpers.base_component import BaseComponent

class SearchWay(BaseComponent):

    selectors = {
        'self': '.searchBar__tab.searchBar__rsTab',
        'input1': '//*[@id="module-1-1-2"]/div/input',
        'input2': '//*[@id="module-1-1-3"]/div/input',
        'submit': '.searchBar__submit._rs'
    }

    def search(self, pointA, pointB):
        self.driver.find_element_by_css_selector(self.selectors['self']).click()
        self.driver.find_element_by_xpath(self.selectors['input1']).send_keys(pointA)
        self.driver.find_element_by_xpath(self.selectors['input2']).send_keys(pointB)
        self.driver.find_element_by_css_selector(self.selectors['submit']).submit()
