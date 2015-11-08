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

class SpotifyTest(unittest.TestCase):
    def __init__(self, name, driver, config):
        super(SpotifyTest, self).__init__(name)
        self.driver = driver
        self.config = config

    def test_spotify(self):
        self.driver.get("https://play.spotify.com")
        try:
            self.driver.find_element_by_id("has-account").click()
            self.driver.find_element_by_id("login-usr").clear()
            self.driver.find_element_by_id("login-usr").send_keys(self.config['websites']['spotify']['login'])
            self.driver.find_element_by_id("login-pass").clear()
            self.driver.find_element_by_id("login-pass").send_keys(self.config['websites']['spotify']['pass'])
            self.driver.find_element_by_css_selector("#sp-login-form > div > button").click()
        except NoSuchElementException:
            pass
        self.driver.get("https://play.spotify.com/album/2mCuMNdJkoyiXFhsQCLLqw")
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.front > iframe')))
        except TimeoutException:
            self.fail()
        self.driver.switch_to_frame(self.driver.find_element_by_css_selector("div.front > iframe"))
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'album-page')))
        except TimeoutException:
            self.fail()
        try:
            WebDriverWait(self.driver, 5).until(EC.title_contains('▶'))
        except TimeoutException:
            try:
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.button-play')))
            except TimeoutException:
                self.fail()
            self.driver.find_element_by_css_selector("button.button-play").click()
        try:
            WebDriverWait(self.driver, 10).until(EC.title_contains('▶'))
        except TimeoutException:
            self.fail()
        self.assertEqual("▶ Never Gonna Give You Up - Rick Astley - Spotify", self.driver.title)
        time.sleep(10)
        self.assertEqual({'albumName': NO_INFO_STRING,
                         'artistName': 'Rick Astley',
                         'duration': '3:33',
                         'nowPlaying': 'Rick Astley - Never Gonna Give You Up',
                         'trackName' : 'Never Gonna Give You Up',
                         'url': 'https://play.spotify.com/track/6JEK0CvvjDjjMUBFoXShNZ'}
                        , readResults(self.config))
