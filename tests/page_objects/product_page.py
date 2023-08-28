import pandas as pd
from page_objects.common_ops import CommonOps
from page_objects.common_ops import findByXpath
import time

class ProductPage(CommonOps):
    
    df = pd.read_csv("women.csv")
    def __init__(self, driver):
        super().__init__(driver)
        self.colorOne = findByXpath(self, "//a[@title='Orange']")
        self.colorTwo = findByXpath(self, "//a[@title='Blue']")


    def checkColor(self):
      self.colorOne.click()
      time.sleep(5)

      #colors from women.csv file
      orangeColor = self.df.iloc[2, 3]
      print(f"color from file....{orangeColor}")
      blueColor = self.df.iloc[4, 3]
      print(f"color from file....{blueColor}")

      #check current url
      currentUrl = self.driver.current_url
      print(f"current url {currentUrl}")

      #verify when users clicks orange color url contains color from file
      expressionOne = orangeColor in currentUrl
      assert expressionOne
      print(expressionOne)

      self.colorTwo.click()
      time.sleep(2)
      currentUrl = self.driver.current_url

      expressionTwo = blueColor in currentUrl
      assert expressionTwo
      print(expressionTwo)