import pytest
from selene.support.shared import browser

from tests.config import device_resolution


@pytest.fixture(params=[pytest.param("Desktop", id="Desktop resolution"),
                        pytest.param("Mobile", id="Mobile resolution")],
                scope="session")
def setup_browser(request):
    browser.config.window_width, browser.config.window_height = device_resolution[request.param]


def test_github_desktop_sign_in(setup_browser):
    if browser.config.window_width < 1080:
        pytest.skip(reason='Test for desktop version, despite mobile resolution was submitted')

    browser.open("https://github.com/")
    browser.element(".HeaderMenu-link--sign-in").click()


def test_github_mobile_sign_in(setup_browser):
    if browser.config.window_width > 1080:
        pytest.skip(reason='Test for mobile version, despite desktop resolution was submitted')

    browser.open("https://github.com/")
    browser.element('.flex-order-2 .Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
