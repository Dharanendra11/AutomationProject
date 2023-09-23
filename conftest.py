import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver

# global driver
# driver = webdriver.Chrome()
#
# #Method for taking screenshots when the test case fails
# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     setattr(item, "rep_" + rep.when, rep)
#     return rep
#
# @pytest.fixture
# def log_on_failure(request):
#     yield
#     item = request.node
#     if item.rep_call.failed:
#        driver.save_screenshot('error.png')


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


