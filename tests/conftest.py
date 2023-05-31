import pytest
from selene import browser



@pytest.fixture(scope='function', autouse=True)
def browser_conf():
    browser.config.window_width = 1600
    browser.config.window_height = 900
    browser.config.base_url = 'https://github.com'
    yield
    browser.quit()