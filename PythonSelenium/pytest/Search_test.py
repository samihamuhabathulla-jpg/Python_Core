import pytest
import read_config
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:

    def test_validate(self):
        keyword = read_config.get_config("search term","valid")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys(keyword)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        assert self.driver.find_element(By.XPATH, "//a[normalize-space()='HP LP3065']").is_displayed()

    def test_invalid(self):
        keyword = read_config.get_config("search term","invalid")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys(keyword)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        kiot = self.driver.find_elements(By.XPATH, "//a[normalize-space()='HP LP3065']")
        assert len(kiot) == 0