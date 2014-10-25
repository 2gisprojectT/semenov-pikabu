from online.helpers.base_component import BaseComponent

class ShareLink(BaseComponent):

    selectors = {
        'self': '.extras__share',
        'button': '.extras__share',
        'link': 'input.share__popupUrlInput'
    }

    def getLink(self):
        self.driver.find_element_by_css_selector(self.selectors['button']).click()
        return self.driver.find_element_by_css_selector(self.selectors['link']).get_attribute("value")

