class Page():
    def __init__(self, driver):

        self.driver = driver
        self._search_bar = None
        self._search_result = None
        self._share_link = None
        self._search_way = None
        self._way_result = None

    @property
    def search_bar(self):
        from online.helpers.search_bar import SearchBar

        if self._search_bar is None:
            self._search_bar = SearchBar(self.driver, self.driver.find_element_by_css_selector(SearchBar.selectors['self']))
        return self._search_bar

    @property
    def share_link(self):
        from online.helpers.sharelink import ShareLink

        if self._share_link is None:
            self._share_link = ShareLink(self.driver, self.driver.find_element_by_css_selector(ShareLink.selectors['self']))
        return self._share_link

    @property
    def search_way_form(self):
        from online.helpers.search_way import SearchWay

        if self._search_way is None:
            self._search_way = SearchWay(self.driver, self.driver.find_element_by_css_selector(SearchWay.selectors['self']))
        return self._search_way

    @property
    def way_result(self):
        from online.helpers.way_result import WayResult

        if self._way_result is None:
            self._way_result = WayResult(self.driver, self.driver.find_element_by_css_selector(WayResult.selectors['self']))
        return self._way_result

    @property
    def search_result(self):
        from online.helpers.search_result import SearchResult

        if self._search_result is None:
            self._search_result = SearchResult(self.driver, self.driver.find_element_by_css_selector(SearchResult.selectors['self']))
        return self._search_result

    def open(self, url):
        self.driver.get(url)