#-*- coding:UTF-8 -*-
from unittest import TestCase
import unittest
from selenium import webdriver
from pikabu.helpers.page import Page

class SeleniumTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(5)
        cls.page = Page(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_short_word(self):
        self.page.search_bar.search(u'щи')
        self.assertEqual(u'щи',
                         self.page.search_bar.search_string,
                         u'Строка поиска не совпадает с запросом')
        self.assertEqual(0,
                         self.page.search_bar.count_results,
                         u'Результатов быть не должно')
        self.assertEqual(u'Слишком короткая фраза для поиска. Фраза должна содержать минимум 3 символа.',
                         self.page.search_bar.search_noresult,
                         u'Строка поиска не совпадает с запросом')

    def test_long_word(self):
        self.page.search_bar.search(u'человеконенавистник')
        self.assertEqual(u'человеконенавистник',
                         self.page.search_bar.search_string,
                         u'Строка поиска не совпадает с запросом')
        self.assertGreater(self.page.search_bar.count_results,
                           0,
                           u'Количество найденных должно быть больше нуля')
        self.assertEqual("False",
                         self.page.search_bar.search_noresult,
                         u'Лжет, что нет результатов')

    def test_two_short_word(self):
        self.page.search_bar.search(u'щи щи')
        self.assertEqual(u'щи щи',
                         self.page.search_bar.search_string,
                         u'Строка поиска не совпадает с запросом')
        self.assertEqual(0, self.page.search_bar.count_results,
                         u'Результатов быть не должно')

if __name__ == '__main__':
    unittest.main()