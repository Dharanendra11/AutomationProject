from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.maximize_window()
wait= WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located("//span[contains(text(),'Cart')]"))
driver.quit()