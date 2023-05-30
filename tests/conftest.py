import pytest
from selene import browser
from selenium import webdriver



@pytest.fixture(scope='function', autouse=True)
def browser_conf():
    chrome_options = webdriver.ChromeOptions()
    browser.config.driver_options = chrome_options
    browser.driver.set_window_size(1600, 900)
    browser.config.base_url = 'https://github.com'