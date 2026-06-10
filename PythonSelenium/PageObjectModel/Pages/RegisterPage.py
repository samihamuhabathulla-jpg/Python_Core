from selenium.webdriver.common.by import By

class RegisterPage:

    def __init__(self, driver):
        self.driver = driver

    def click_dropdown(self):
        self.driver.find_element(By.XPATH, "//span[@class='caret']").click()
    def click_register_link(self):
        self.driver.find_element(By.LINK_TEXT, "Register").click()
    def enter_firstname(self, firstname):
        self.driver.find_element(By.ID, "input-firstname").send_keys(firstname)
    def enter_lastname(self, lastname):
        self.driver.find_element(By.ID, "input-lastname").send_keys(lastname)
    def enter_email(self, email):
        self.driver.find_element(By.ID, "input-email").send_keys(email)
    def enter_telephone(self, telephone):
        self.driver.find_element(By.ID, "input-telephone").send_keys(telephone)
    def enter_password(self, password):
        self.driver.find_element(By.ID, "input-password").send_keys(password)
    def enter_confirm_password(self, password):
        self.driver.find_element(By.ID, "input-confirm").send_keys(password)
    def click_privacy_policy(self):
        self.driver.find_element(By.NAME, "agree").click()
    def click_continue_button(self):
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
    def get_warning_message(self):
        return self.driver.find_element(By.XPATH,"//div[contains(@class,'alert-danger')]").text