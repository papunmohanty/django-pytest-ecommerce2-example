import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def chrome_browser_instance(request):
    """
    Provide a selenium web driver instance
    """
    options = (
        Options()
    )  # Selenium setup: which will find chromedriver.exe or chromedriver file to connect to Chrome browser.
    options.headless = False
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.close()
