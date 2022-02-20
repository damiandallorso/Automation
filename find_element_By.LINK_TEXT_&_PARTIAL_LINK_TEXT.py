import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
class FindByIdName(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://www.techlistic.com/p/selenium-practice-form.html")

    def testId(self):
        elementById = driver.find_element(By.LINK_TEXT, "Automate Amazon like E-Commerce website with Selenium")
        if elementById is not None:
            print("El elemento con LINK_TEXT Automate Amazon like E-Commerce website with Selenium fue encontrado")

    def testName(self):
        elementByName = driver.find_element(By.PARTIAL_LINK_TEXT, "Automate GoDaddy website")
        if elementByName is not None:
            print("El elemento con PARTIAL_LINK_TEXT Automate GoDaddy website fue encontrado")

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()
