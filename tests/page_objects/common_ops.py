from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

class CommonOps():

    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 20)
       # self._action = ActionChains(self.driver)


def wait_for(self, locator):
    return self._wait.until(ec.presence_of_element_located(locator))


def findById(self, locator):
    return self.driver.find_element(By.ID, locator)

def findByXpath(self, locator):
    return self.driver.find_element(By.XPATH, locator)

def findElementsByXpath(self, locator):
    return self.driver.find_elements(By.XPATH, locator)
