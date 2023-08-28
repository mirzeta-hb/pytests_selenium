import pytest
from selenium import webdriver

driver: webdriver
driver = webdriver.Chrome()

@pytest.fixture(scope='function')
def getdriver():
    driver.get("http://www.automationpractice.pl/index.php")
    yield driver

    driver.close()

