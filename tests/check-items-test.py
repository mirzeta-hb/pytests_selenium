from page_objects.account_info import AccountInfo
from page_objects.home_page import HomePage
from page_objects.login_page import LoginPage
from page_objects.women_page import WomenPage
from page_objects.product_page import ProductPage


def test_login_to_website(getdriver):
    
    homePage = HomePage(getdriver)
    homePage.clickSignIn()
    loginPage = LoginPage(getdriver)
    loginPage.loginToMyShop()

    accountPage = AccountInfo(getdriver)
    accountPage.clickWomenTab()

    womenPage = WomenPage(getdriver)
    womenPage.checkDisplayedItems()
    womenPage.openItemDetails()

    productPage = ProductPage(getdriver)
    productPage.checkColor()