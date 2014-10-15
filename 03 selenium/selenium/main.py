# =*- coding: utf-8 -*-
__author__ = 'SemenovEvgeniy'

from unittest import TestCase
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class SeleniumTest(TestCase):
    def test_EmailTest(self):
        driver = webdriver.Firefox()
        driver.get("http://www.pikabu.ru")
        driver.find_element_by_id("login_block_btn_reg").click()
        email = driver.find_element_by_id("rm_email")
        email.clear()
        email.send_keys("123@123")
        driver.find_element_by_id("rm_pass").click()
        element = driver.find_element_by_id("rm_email_err")
        assert "Неверный email", element.text
        driver.close()

if __name__ == '__main__':
    unittest.main()