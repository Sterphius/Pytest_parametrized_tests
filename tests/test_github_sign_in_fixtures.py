import pytest
from selene.support.shared import browser
from tests.config import device_resolution


@pytest.fixture(scope='session')
def mobile_browser():
    browser.config.window_width, browser.config.window_height = device_resolution['Mobile']


@pytest.fixture(scope='session')
def desktop_browser():
    browser.config.window_width, browser.config.window_height = device_resolution['Desktop']


def test_github_desktop_sign_in(desktop_browser):
    browser.open("https://github.com/")
    browser.element(".HeaderMenu-link--sign-in").click()


def test_github_mobile_sign_in(mobile_browser):
    browser.open("https://github.com/")
    browser.element('.flex-order-2 .Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
