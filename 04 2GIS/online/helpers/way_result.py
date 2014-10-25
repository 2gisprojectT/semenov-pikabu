from online.helpers.base_component import BaseComponent

class WayResult(BaseComponent):
    selectors = {
        'self': '#module-1-9-1-1'
    }

    @property
    def is_displayed(self):
        return self.driver.find_element_by_css_selector(self.selectors['self']).is_displayed()