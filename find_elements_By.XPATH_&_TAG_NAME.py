import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class FindByIdName(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://www.techlistic.com/p/selenium-practice-form.html")

    def testId(self):
        filas = driver.find_elements(By.XPATH, "//*[@id='post-body-3077692503353518311']/div[1]/div/div/h2[2]/div[1]/div/div[20]/label")
        if filas is not None:
            elementos = len(filas)
            print("Encontré: ", elementos)

    def testtag(self):
        filas = driver.find_elements(By.TAG_NAME, "h2")
        if filas is not None:
            elementos = len(filas)
            print("Encontré: ", elementos)

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()
