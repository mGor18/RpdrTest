import pytest
from selenium import webdriver

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup_driver(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    elif browser_name == "IE":
        driver = webdriver.Ie(executable_path="C:\\IEDriverServer.exe")
    else:
        raise Exception("{browser} is not a valid browser".format(browser="browser_name"))

    driver.get("http://localhost:3000/")
    driver.maximize_window()
    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield
    driver.close()
