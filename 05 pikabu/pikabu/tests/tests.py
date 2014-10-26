#-*- coding:UTF-8 -*-
from unittest import TestCase
import unittest
from selenium import webdriver
from pikabu.helpers.page import Page

class SeleniumTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.page = Page(self.driver)
        self.page.open("http://pikabu.ru")

    def tearDown(self):
        self.driver.quit()

    def test_search(self):
        self.page.search_bar.search("123323443")

if __name__ == '__main__':
    unittest.main()