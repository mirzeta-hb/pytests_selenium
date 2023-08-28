import pandas as pd
from page_objects.home_page import HomePage
from page_objects.register_page import RegisterPage
from page_objects.account_info import AccountInfo
import time

from page_objects.login_page import LoginPage


def test_open_url(getdriver):
      homePage = HomePage(getdriver)
      homePage.clickSignIn()

      loginPage = LoginPage(getdriver)
      loginPage.typeEmail()
      time.sleep(5)

      registerPage = RegisterPage(getdriver)
      registerPage.selectGender()
      registerPage.populateUserInfo()
      registerPage.selectDateOfBirth()
      registerPage.clickSubmitReg()


      accountPage = AccountInfo(getdriver)
      accountPage.checkAccountMessage
