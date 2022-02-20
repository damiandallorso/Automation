import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class FindByIdName (unittest.TestCase):

    def setUp(self):
        global driver 
        driver = webdriver.Chrome()
        driver.get("https://www.techlistic.com/p/selenium-practice-form.html")

    def testIdName(self):
        elementById = driver.find_element(By.ID, "profession-0")
        if elementById is not None:
            print("El elemento con ID profession-0 fue encontrado")

        elementByName = driver.find_element(By.NAME, "continents")
        if elementByName is not None:
            print("El elemento con NAME continents fue encontrado")

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
    unittest.main()
