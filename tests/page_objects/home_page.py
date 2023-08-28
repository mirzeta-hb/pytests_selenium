from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from page_objects.common_ops import CommonOps, findById


class HomePage(CommonOps):
   

   def __init__(self, driver):
       super().__init__(driver)
       self.sign_in_button = (By.XPATH, "//div[@class='header_user_info']/a")
     
     
   def clickSignIn(self):
       el = self._wait.until(ec.presence_of_element_located(self.sign_in_button))
       el.click()


        


