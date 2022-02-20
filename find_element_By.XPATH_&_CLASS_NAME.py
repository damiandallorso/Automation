import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class FindByIdName(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://www.techlistic.com/p/selenium-practice-form.html")

    def testId(self):
        elementByXpath = driver.find_element(By.XPATH, "//*[@id='post-body-3077692503353518311']/div[1]/div/div/h2[2]/div[3]/div[1]/div[1]/b")
        if elementByXpath is not None:
            print("El elemento con ID post-body-3077692503353518311 fue encontrado")

    def testName(self):
        elementByName = driver.find_element(By.CLASS_NAME, "control-group")
        if elementByName is not None:
            print("El elemento con CLASS_NAME control-group fue encontrado")

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()
