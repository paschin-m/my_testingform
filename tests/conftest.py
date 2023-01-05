import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1200,800')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(executable_path=os.getcwd()+'''../venv/Scripts''', options=options)
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver=get_webdriver
    url = 'https://avito.ru'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()