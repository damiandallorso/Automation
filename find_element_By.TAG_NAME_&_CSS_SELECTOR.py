import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class FindByIdName(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://www.techlistic.com/p/selenium-practice-form.html")

    def testId(self):
        elementById = driver.find_element(By.TAG_NAME, "h2")
        if elementById is not None:
            print("El elemento con TAG_NAME h2 fue encontrado")

    def testName(self):
        elementByName = driver.find_element(By.CSS_SELECTOR, "#post-body-3077692503353518311 > div:nth-child(1) > div > div > h2:nth-child(2) > div:nth-child(1) > div > div:nth-child(25)")
        if elementByName is not None:
            print("El elemento con CSS_SELECTOR #post-body-3077692503353518311 fue encontrado")

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()
