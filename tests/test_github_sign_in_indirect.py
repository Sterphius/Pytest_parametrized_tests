import pytest
from selene.support.shared import browser

from tests.config import device_resolution


@pytest.fixture(params=[pytest.param("Desktop", id="Desktop resolution"),
                        pytest.param("Mobile", id="Mobile resolution")],
                scope="session")
def setup_browser(request):
    browser.config.window_width, browser.config.window_height = device_resolution[request.param]


mobile_resolution = pytest.mark.parametrize("setup_browser", ["Mobile"], indirect=True)
desktop_resolution = pytest.mark.parametrize("setup_browser", ["Desktop"], indirect=True)


@desktop_resolution
def test_github_desktop_sign_in(setup_browser):
    browser.open("https://github.com/")
    browser.element(".HeaderMenu-link--sign-in").click()


@mobile_resolution
def test_github_mobile_sign_in(setup_browser):
    browser.open("https://github.com/")
    browser.element('.flex-order-2 .Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
