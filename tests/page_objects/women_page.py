import time
from page_objects.common_ops import CommonOps, findElementsByXpath, findByXpath
import pandas as pd


class WomenPage(CommonOps):
   
    df = pd.read_csv("women.csv")

    def __init__(self, driver):
     super().__init__(driver)
     self.itemsName =  findElementsByXpath(self, "//a[@class= 'product-name']")
     self.firstItem = findByXpath(self,"//ul[@class='product_list grid row']/li[1]")
     self.moreButton = findByXpath(self, "//span[text() = 'More']")
     self.newPrice = "//a[contains(text(),'Printed Summer Dress')]/following::div/span[contains(text(), '{}')]"

    


    def checkDisplayedItems(self):
     firstItemFromFile = self.df.iloc[0,1]

     for element in self.itemsName:
       print(element.text)

     assert self.itemsName[1].text == firstItemFromFile


    def openItemDetails(self):
      self.firstItem.click()
      time.sleep(10)
      
      self.moreButton.click()


    def checkNewPriceIsDisplayed(self):
      expectedPrice = self.df.loc[4, "Price"]
      updatedXpathWithNewPrice = self.newPrice.format(expectedPrice)
      newPrice = findByXpath(self, updatedXpathWithNewPrice)

      assert newPrice.is_displayed()
