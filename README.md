# UNP-tests
Functional tests for Untamed-Now-Playing

How to
--------------------------------------

### Requirement:
Python >= 3.4 required (python 2.7.x may work).

Python bindinds for Selenium: http://selenium-python.readthedocs.org/installation.html#downloading-python-bindings-for-selenium

It should works under Windows, but I wrote this (and use this) under Linux only.

### Configuration:
Rename `config.yml.sample` to `config.yml` and fill it with your informations (I may consider some kind of encryption in the future, I don't really like having all my password in one raw file).

UNP must be installed on the specified Firefox profile and must be configured to "Multiple txt files".

### Run:

    python3 start.py
