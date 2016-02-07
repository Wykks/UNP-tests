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

class SoundcloudTest(unittest.TestCase):
    def __init__(self, name, driver, config):
        super(SoundcloudTest, self).__init__(name)
        self.driver = driver
        self.config = config

    def test_soundcloud(self):
        self.driver.get("https://soundcloud.com/nils-official/rick-astley-feat-avicii-never")
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.playControls__inner')))
        except TimeoutException:
            self.fail()
        self.assertTrue(self.driver.title.startswith("AVICII vs RICK ASTLEY"))
        time.sleep(10)
        self.assertEqual({'albumName': NO_INFO_STRING,
                         'artistName': 'AVICII vs RICK ASTLEY',
                         'duration': '4:26',
                         'nowPlaying': 'AVICII vs RICK ASTLEY - Never Gonna Wake You Up (Get Knocked...',
                         'trackName' : 'Never Gonna Wake You Up (Get Knocked Down) (NilsOfficial Mas...',
                         'url': 'http://soundcloud.com/nils-official/rick-astley-feat-avicii-never'}
                        , readResults(self.config))
