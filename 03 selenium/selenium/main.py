# =*- coding: utf-8 -*-
__author__ = 'SemenovEvgeniy'

from unittest import TestCase
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class SeleniumTest(TestCase):

    def test_IncorrectEmail(self):
        driver = webdriver.Firefox()
        driver.get("http://www.pikabu.ru")
        driver.find_element_by_id("login_block_btn_reg").click()
        email = driver.find_element_by_id("rm_email")
        email.clear()
        email.send_keys("@")
        driver.find_element_by_id("rm_pass").click()
        element = driver.find_element_by_id("rm_email_err")
        driver.close()
        assert u'Неверный email'==element.text

    def test_CorrectEmail(self):
        driver = webdriver.Firefox()
        driver.get("http://www.pikabu.ru")
        driver.find_element_by_id("login_block_btn_reg").click()
        email = driver.find_element_by_id("rm_email")
        email.clear()
        email.send_keys("123@123.ru")
        driver.find_element_by_id("rm_pass").click()
        element = driver.find_element_by_id("rm_email_err")
        driver.close()
        assert element.text==""

if __name__ == '__main__':
    unittest.main()