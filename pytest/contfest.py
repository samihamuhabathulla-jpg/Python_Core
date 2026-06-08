from urllib import request

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import D


@pytest.fixture()
def test_setup_and_teardown():
    d=webdriver.Chrome()
    d.maximize_window()
    d.implicitly_wait(10)
    d.get("https://tutorialsninja.com/demo/")
    request.cls.d=d
    yield
    d.quit()