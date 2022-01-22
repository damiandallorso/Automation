from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get("https://demoqa.com")
elemento = driver.find_element(By.ID, "adplus-anchor")
if elemento is not None:
    print("El elemento fue encontrado")
driver.quit()
