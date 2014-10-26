class Page():
    def __init__(self, driver):
        self.driver = driver
        self._search_bar = None

    @property
    def search_bar(self):
        from pikabu.helpers.search_bar import SearchBar

        if self._search_bar == None:
            self._search_bar = SearchBar(self.driver)
        return self._search_bar

    def open(self, query):
        self.driver.get(query)
