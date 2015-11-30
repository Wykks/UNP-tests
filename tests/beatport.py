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

class BeatportTest(unittest.TestCase):
    def __init__(self, name, driver, config):
        super(BeatportTest, self).__init__(name)
        self.driver = driver
        self.config = config

    def test_beatport(self):
        self.driver.get("https://www.beatport.com/spinninrecords/tracks/ousncwiobsj7/on-the-run-extended-mix")
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.audio-control--button')))
        except TimeoutException:
            self.fail()
        self.assertTrue(self.driver.title.startswith("On The Run"))
        self.driver.find_element_by_css_selector(".audio-control--button").click()
        time.sleep(15)
        self.assertEqual({'albumName': NO_INFO_STRING,
                         'artistName': 'Ummet Ozcan',
                         'duration': '4:07',
                         'nowPlaying': 'Ummet Ozcan - On The Run',
                         'trackName' : 'On The Run',
                         'url': 'https://www.beatport.com/spinninrecords/tracks/ousncwiobsj7/on-the-run-extended-mix'}
                        , readResults(self.config))
