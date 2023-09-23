import json
from time import sleep
import ordlookup

from selenium import webdriver
driver=webdriver.Chrome()

driver.execute_cdp_cmd("Network.enable",cmd_args={})
driver.execute_cdp_cmd("Network.responseReceived",cmd_args={})

driver.get("http://google.com")

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture() #fixtures can be kept in a separate file called conftest.py and passed as a argument. If autouse=True is set for
#fixture we don't need to pass it as argument s well
def setUp():
    print("Launch browser")
    print("Login")
    yield # Will be executed at the end
    print("Logout")
    print("Close browser")


@pytest.mark.skip
def test_home2(setUp):
    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    print(driver.title)
    driver.quit()

#@pytest.mark.parameterize("test_input",expected,[("1+2",3),("2+6",10)])