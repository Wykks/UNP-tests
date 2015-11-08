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

class EightTrackTest(unittest.TestCase):
    def __init__(self, name, driver, config):
        super(EightTrackTest, self).__init__(name)
        self.driver = driver
        self.config = config

    def test_8tracks(self):
        self.driver.get("http://8tracks.com/swegglet/rickroll")
        self.assertTrue(self.driver.title.startswith("8tracks radio | Rickroll"))
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'play_overlay')))
        except TimeoutException:
            self.fail()
        self.driver.find_element_by_css_selector("#play_overlay").click()
        time.sleep(15)
        self.assertEqual({'albumName': 'Never Gonna Give You Up',
                         'artistName': 'Rick Astley',
                         'duration': NO_INFO_STRING,
                         'nowPlaying': 'Rick Astley - Never Gonna Give You Up',
                         'trackName' : 'Never Gonna Give You Up',
                         'url': 'http://8tracks.com/swegglet/rickroll'}
                        , readResults(self.config))
