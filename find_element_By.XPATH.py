import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClickSendKeys(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://www.techlistic.com/p/selenium-practice-form.html")

    def testId(self):
        liga = driver.find_element(By.XPATH, "//*[@id='profession-1']")
        if liga is not None:
            liga.click()

        nombre = driver.find_element(By.XPATH, "//*[@id='datepicker']")
        if nombre is not None:
            nombre.send_keys("01/07/1995")
        time.sleep(5)

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()
