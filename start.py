#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time, re
from yaml import load

from utils import *
from tests.deezer import DeezerTest
from tests.eighttracks import EightTrackTest
from tests.spotify import SpotifyTest
from tests.beatport import BeatportTest
from tests.youtube import YoutubeTest

def loadConfig():
    with open('config.yml', encoding='utf-8') as credsFile:
        data = load(credsFile)
    return data

if __name__ == "__main__":
    config = loadConfig()
    profile = webdriver.FirefoxProfile(config['firefox_profile'])
    #profile.set_preference('webdriver.load.strategy', 'unstable')
    driver = webdriver.Firefox(profile)
    try:
        suite = unittest.TestSuite()
        suite.addTest(DeezerTest('test_deezer', driver, config))
        suite.addTest(EightTrackTest('test_8tracks', driver, config))
        suite.addTest(SpotifyTest('test_spotify', driver, config))
        suite.addTest(BeatportTest('test_beatport', driver, config))
        suite.addTest(YoutubeTest('test_youtube', driver, config))
        unittest.TextTestRunner(verbosity=2).run(suite)
    finally:
        driver.quit()
