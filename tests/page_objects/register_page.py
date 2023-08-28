from page_objects.common_ops import CommonOps, findByXpath , findById, wait_for
import pandas as pd
from selenium.webdriver.common.by import By
import time

class RegisterPage(CommonOps): 


    def __init__(self, driver):
        super().__init__(driver)
        self.gender_field = (By.XPATH, "//input[@id= 'id_gender2']")
        self.first_name = findById(self, 'customer_firstname')
        self.last_name = findById(self, 'customer_lastname')
        self.email = findById(self, 'email' )
        self.password = findById(self, 'passwd' )
        self.day = findByXpath(self, "//select[@id='days']/option[@value = '1']" )
        self.month = findByXpath(self, "//select[@id='months']/option[@value='2']" )
        self.year = findByXpath(self, "//select[@id='years']/option[@value='1992']")
        self.submit_button = findByXpath(self, "//button[@id='submitAccount']")


    def selectGender(self):
     gender = wait_for(self, self.gender_field)
     gender.click()


    def populateUserInfo(self):
       read_data = pd.read_csv("users.csv")
       time.sleep(5)
       self.first_name.send_keys(read_data["FirstName"])
       self.last_name.send_keys(read_data["LastName"])
       self.password.send_keys(read_data["Password"])


    def selectDateOfBirth(self):
      self.day.click()
      self.month.click()
      self.year.click()

    def clickSubmitReg(self):
       self.submit_button.click()