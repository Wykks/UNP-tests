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

class YoutubeTvTest(unittest.TestCase):
    def __init__(self, name, driver, config):
        super(YoutubeTvTest, self).__init__(name)
        self.driver = driver
        self.config = config

    def test_youtubetv(self):
        self.driver.get("https://www.youtube.com/tv#/watch?v=dQw4w9WgXcQ")
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#player-controls')))
        except TimeoutException:
            self.fail()
        self.assertEqual("YouTube TV", self.driver.title)
        time.sleep(5)
        self.assertEqual({'albumName': NO_INFO_STRING,
                         'artistName': 'Rick Astley',
                         'duration': '3:33',
                         'nowPlaying': 'Rick Astley - Never Gonna Give You Up',
                         'trackName' : 'Never Gonna Give You Up',
                         'url': 'https://www.youtube.com/tv#/watch?v=dQw4w9WgXcQ&resume'}
                        , readResults(self.config))
