import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

options_chrome = Options()
options_chrome.set_preference("intl.accept_languages", 'en-GB')
service_chrome = Service(r'D:\programs\Python\chromedriver_win32\chromedriver.exe')

options_firefox = Options()
options_firefox.set_preference("intl.accept_languages", 'en-GB')
service_firefox = Service(r'D:\programs\Python\geckodriver-v0.30.0-win64\geckodriver.exe') 


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options_chrome, service=service_chrome)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=options_firefox, service=service_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()