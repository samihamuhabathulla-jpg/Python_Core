from selenium.webdriver.common.by import By

class SearchPage:

    def __init__(self, driver):
        self.driver = driver
    def enter_product(self, product):
        self.driver.find_element(By.NAME, "search").send_keys(product)
    def click_search(self):
        self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
    def product_displayed(self):
        return self.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()
    def get_error_message(self):
        return self.driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text