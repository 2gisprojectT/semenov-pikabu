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
                         self.page.search_bar.search_too_short_query,
                         u'Нет сообщения о слишком коротком запросе')

    def test_long_word(self):
        self.page.search_bar.search(u'человеконенавистник')
        self.assertEqual(u'человеконенавистник',
                         self.page.search_bar.search_string,
                         u'Строка поиска не совпадает с запросом')
        self.assertGreater(self.page.search_bar.count_results,
                           0,
                           u'Количество найденных должно быть больше нуля')
        self.assertEqual("False",
                         self.page.search_bar.search_too_short_query,
                         u'Лжет, что слишком короткая строка запроса')

    def test_two_short_word(self):
        self.page.search_bar.search(u'щи щи')
        self.assertEqual(u'щи щи',
                         self.page.search_bar.search_string,
                         u'Строка поиска не совпадает с запросом')
        self.assertEqual(0, self.page.search_bar.count_results,
                         u'Результатов быть не должно')
        self.assertEqual("False",
                         self.page.search_bar.search_too_short_query,
                         u'Лжет, что слишком короткая строка запроса')

    def test_nonexistent_word(self):
        self.page.search_bar.search(u'авсмм')
        self.assertEqual(u'авсмм',
                         self.page.search_bar.search_string,
                         u'Строка поиска не совпадает с запросом')
        self.assertEqual(0, self.page.search_bar.count_results,
                         u'Результатов быть не должно')
        self.assertEqual("False",
                         self.page.search_bar.search_too_short_query,
                         u'Лжет, что слишком короткая строка запроса')

    def test_backslash(self):
        self.page.search_bar.search(u'\\')
        self.assertEqual(u'\\',
                         self.page.search_bar.search_string,
                         u'Строка поиска не совпадает с запросом')
        self.assertEqual(0, self.page.search_bar.count_results,
                         u'Результатов быть не должно')
        self.assertEqual(u'Слишком короткая фраза для поиска. Фраза должна содержать минимум 3 символа.',
                         self.page.search_bar.search_too_short_query,
                         u'Нет сообщения о слишком коротком запросе')

if __name__ == '__main__':
    unittest.main()