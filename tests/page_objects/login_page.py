from datetime import datetime
import time
from page_objects.common_ops import CommonOps
from page_objects.common_ops import findById
import pandas as pd

class LoginPage(CommonOps):

     
    def __init__(self, driver):
        super().__init__(driver)
        self.email = findById(self,"email")
        self.password = findById(self,"passwd")
        self.submitButton = findById(self,"SubmitLogin")
        self.input_email_field = findById(self, 'email_create')
        self.submit_button = findById(self, 'SubmitCreate' )



    def typeEmail(self):
        current_datetime = datetime.now()
        current_time = current_datetime.strftime("%m/%d/%Y%H%M%S")
        email = f"{current_time}email1@hotmail.com"
        df = pd.read_csv('users.csv')
        df["Email"] = email
        df.to_csv('users.csv')

        self.input_email_field.send_keys(email)
        self.submit_button .click()



    def loginToMyShop(self):
       
        df = pd.read_csv("users.csv")
        username = df["Email"]
        password = df["Password"]

        self.email .send_keys(username)
        self.password.send_keys(password)
        self.submitButton .click()
        time.sleep(5)
