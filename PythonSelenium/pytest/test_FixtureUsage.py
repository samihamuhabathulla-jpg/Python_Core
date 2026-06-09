import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def test_setup_and_teardown():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://tutorialsninja.com/demo/")
    yield driver
    driver.quit()


