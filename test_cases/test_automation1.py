import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.first
def test_homepage():
    driver=webdriver.Chrome()

    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    time.sleep(10)
    print(driver.title)
    driver.quit()

@pytest.mark.skip
def test_home2():
    driver=webdriver.Chrome()

    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    print(driver.title)
    driver.quit()

    
