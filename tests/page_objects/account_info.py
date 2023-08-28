from page_objects.common_ops import CommonOps, findByXpath


class AccountInfo(CommonOps):   

    def __init__(self, driver):
        super().__init__(driver)
        self.account_info = findByXpath(self, "//p[@class= 'info-account']")
        self.womenTab = findByXpath(self, "//a[@title='Women']")

    def checkAccountMessage(self):
     assert self.account_info.text == "Welcome to your account. Here you can manage all of your personal information and orders."


    def clickWomenTab(self):
        self.womenTab.click()
    

