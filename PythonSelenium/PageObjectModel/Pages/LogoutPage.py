from selenium.webdriver.common.by import By

class LogoutPage:

    def __init__(self, driver):
        self.driver = driver

    def click_dropdown(self):
        self.driver.find_element(By.XPATH, "//span[@class='caret']").click()
    def click_login(self):
        self.driver.find_element(By.XPATH, "//a[text()='Login']").click()
    def enter_email(self, email):
        self.driver.find_element(By.XPATH,"(//div[@class='form-group'])[1]/child::input").send_keys(email)
    def enter_password(self, password):
        self.driver.find_element(By.XPATH,"(//div[@class='form-group'])[2]/child::input").send_keys(password)
    def click_login_button(self):
        self.driver.find_element(By.XPATH,"//input[@type='submit']").click()
    def click_my_account(self):
        self.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT,"Logout").click()
    def verify_logout(self):
        return self.driver.find_element(By.XPATH,"//h1[text()='Account Logout']").is_displayed()