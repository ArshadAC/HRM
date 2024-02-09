import pytest
from selenium import webdriver

# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome()
#     driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#     driver.maximize_window()
#     driver.implicitly_wait(5)
#     return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Printing Chrome Browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver = webdriver.Edge()
    else:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver
