from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_homepage():
    driver=webdriver.Chrome()
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    # wait= WebDriverWait(driver,60)
    # wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//span[contains(text(),'Cart')]")))
    print(driver.title)
    driver.quit()