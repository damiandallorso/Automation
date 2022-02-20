from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
elemento = driver.find_element(By.NAME, "photo")
if elemento is not None:
    print("El NAME photo fue encontrado")
driver.quit()
