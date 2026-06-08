import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.mark.parametrize( "input_browser",['chrome', 'firefox'])
@pytest.mark.parametrize("input_url",['https://www.flipkart.com', 'https://www.amazon.com'])

def test_url_on_browser(input_browser, input_url):
    if input_browser == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless")
        web_driver = webdriver.Chrome(options=chrome_options)
    if input_browser == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--headless")
        web_driver = webdriver.Firefox(options=firefox_options)
    web_driver.maximize_window()
    web_driver.get(input_url)
    print("Browser :", input_browser)
    print("URL :", input_url)
    print("Title :", web_driver.title)
    time.sleep(5)
    web_driver.close()