import time
import urllib
import pytest
from selenium import webdriver
from urllib import parse
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


@pytest.mark.flipkart
def test_home2():
    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    print(driver.title)
    current_url = driver.current_url
    # parsed_url = urllib.parse.urlparse(current_url)
    # protocol = parsed_url.scheme
    # domain = parsed_url.netloc
    new_url = urllib.parse.urljoin(current_url,'/cart')
    driver.get(new_url)
    time.sleep(5)

    driver.quit()

#@pytest.mark.parameterize("test_input",expected,[("1+2",3),("2+6",10)])