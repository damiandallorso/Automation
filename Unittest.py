import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class FindByIdName (unittest.TestCase):

    def setUp(self):
        global driver 
        driver = webdriver.Firefox()
        driver.get("https://demoqa.com/")

    def testIdName(self):
        elementById = driver.find_element(By.ID, "adplus-anchor")
        if elementById is not None:
            print("Encontramos el elemento con Id = adplus-anchor")

        elementByName = driver.find_element(By.NAME, "viewport")
        if elementByName is not None:
            print("Encontramos el elemento con name = viewport")

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
    unittest.main()
