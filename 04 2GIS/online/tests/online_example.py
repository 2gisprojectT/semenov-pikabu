#-*- coding:UTF-8 -*-
from unittest import TestCase
import unittest
from selenium import webdriver
from online.helpers.page import Page

class SeleniumTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.page = Page(self.driver)
        self.page.open("http://2gis.ru")

    def test_link(self):
        request = u'кофе'
        self.page.search_bar.search(request)
        link = self.page.share_link.getLink()
        self.page.open(link)
        self.assertEqual(request, self.page.search_bar.request)

    def test_way(self):
        pointA = u'Новосибирск Блюхера 32/1'
        pointB = u'Сакко и Ванцетти, 42'
        self.page.search_way_form.search(pointA, pointB)
        #self.page.search_way_form.search(u'Новосибирск Блюхера 32/1', u'Сакко и Ванцетти, 42')
        self.assertTrue(self.page.way_result.is_displayed)

    def tearDown(self):
       self.driver.quit()

if __name__ == '__main__':
    unittest.main()