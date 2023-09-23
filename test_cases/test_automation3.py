# import requests
# session = requests.session()
# url = r"https://google.com"
# page = session.get(url)
# print(page.status_code)
import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


#@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.yelp
def test_launchGoogle(browser):
    assert browser == 'chrome','Browser not available'
    driver = webdriver.Chrome()
    driver.get("https://www.yelp.com/")
    driver.maximize_window()
    WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located((By.NAME,'find_desc')))
    driver.find_element(By.NAME,'find_desc').send_keys('Hospital')
    driver.find_element(By.NAME, 'find_desc').send_keys(Keys.ENTER)
    WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located((By.XPATH,'//span[text()="Top 10 Best Hospital Near San Francisco, California"]')))
    # hos = driver.find_element(By.XPATH, '//a[contains(text(),"Zuckerberg San Francisco General Hospital and Trauma Center")]')
    # driver.execute_script("arguments[0].scrollIntoView();",hos)
    # time.sleep(2)
    driver.find_element(By.XPATH, '//a[contains(text(),"Zuckerberg San Francisco General Hospital and Trauma Center")]').click()
    time.sleep(10)
    handles = driver.window_handles
    driver.switch_to.window(handles[1])
    time.sleep(5)
    print("Contact No:" + driver.find_element(By.XPATH,"//p[text()='Phone number']/following::p").text)
    # driver.switch_to.window(handles[0])
    driver.find_element(By.XPATH, "//p[text()='Business website']/following::p/a").click()
    handles = driver.window_handles
    driver.switch_to.window(handles[2])

    WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[contains(text(),'University of California')]")))
    hospital_website = driver.current_url
    print(hospital_website)
    time.sleep(2)
    driver.quit()




# def test_launchYoutube(browser):
#     assert browser == 'chrome','Browser not available'
#     driver = webdriver.Chrome()
#     driver.get("https://youtube.com")
#     time.sleep(10)
#     driver.quit()