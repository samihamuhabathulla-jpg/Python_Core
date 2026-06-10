from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
    def click_dropdown(self):
        self.driver.find_element(By.XPATH,"//span[@class='caret']").click()
    def click_login_link(self):
        self.driver.find_element(By.XPATH,"//a[text()='Login']").click()
    def enter_email(self, email):
        self.driver.find_element(By.XPATH,"(//div[@class='form-group'])[1]/child::input").send_keys(email)
    def enter_password(self, password):
        self.driver.find_element(By.XPATH,"(//div[@class='form-group'])[2]/child::input").send_keys(password)
    def click_login_button(self):
        self.driver.find_element(By.XPATH,"//input[@type='submit']").click()
    def verify_login(self):
        return self.driver.find_element(By.XPATH,"//h2[text()='My Account']").is_displayed()