import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClickSendKeys(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://www.techlistic.com/p/selenium-practice-form.html")

    def test1(self):
        print ("profession")
        buton1 = driver.find_element(By.ID, "profession-0")
        if buton1 is not None:
            buton1.click()

        time.sleep(5)

        buton2 = driver.find_element(By.ID, "profession-1")
        if buton2 is not None:
            buton2.click()
            
        time.sleep(5)

    def test2(self):
        print ("tool")
        buton1 = driver.find_element(By.ID, "tool-0")
        if buton1 is not None:
            buton1.click()

        time.sleep(5)

        buton2 = driver.find_element(By.ID, "tool-2")
        if buton2 is not None:
            buton2.click()
            
        time.sleep(5)
        
    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()
