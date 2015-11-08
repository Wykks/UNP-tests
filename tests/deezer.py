#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

from utils import *

class DeezerTest(unittest.TestCase):
    def __init__(self, name, driver, config):
        super(DeezerTest, self).__init__(name)
        self.driver = driver
        self.config = config

    def test_deezer(self):
        self.driver.get("http://www.deezer.com/login")
        try:
            self.driver.find_element_by_id("login_mail").clear()
            self.driver.find_element_by_id("login_mail").send_keys(self.config['websites']['deezer']['login'])
            self.driver.find_element_by_id("login_password").clear()
            self.driver.find_element_by_id("login_password").send_keys(self.config['websites']['deezer']['pass'])
            self.driver.find_element_by_id("login_form_submit").click()
        except NoSuchElementException:
            pass
        self.driver.get("http://www.deezer.com/album/7261054")
        self.assertEqual("Never Gonna Give You Up - The Rickrollerz", self.driver.title)
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.picture-link')))
        except TimeoutException:
            self.fail()
        self.driver.find_element_by_css_selector("a.picture-link").click()
        time.sleep(10)
        self.assertEqual({'albumName': NO_INFO_STRING,
                         'artistName': 'The Rickrollerz',
                         'duration': '03:01',
                         'nowPlaying': 'The Rickrollerz - Never Gonna Give You Up',
                         'trackName' : 'Never Gonna Give You Up',
                         'url': 'http://www.deezer.com/album/7261054'}
                        , readResults(self.config))
