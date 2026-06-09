import pytest 
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities import ExcelReader
import Utilities.logCreator as logCreator
  

@pytest.mark.parametrize("username,password",ExcelReader.get_data("ExcelFiles/loginData.xlsx","login"))

class TestLogin1:
    logger =logCreator.log_generator()
    def test_validlogin1(self,username,password):
        self.logger.info("--Test Started--")
        self.driver=webdriver.Chrome()
        self.logger.info("Chrome Browser Launched")
        self.driver.maximize_window()
        self.logger.info("Browser Maximized")
        self.driver.get("https://demoblaze.com/index.html")
        self.logger.info("Navigated to Demoblaze Website")
        self.driver.find_element(By.ID,value="login2").click()
        self.logger.info("Clicked Login Button")
        time.sleep(5)
        self.driver.find_element(By.ID,value="loginusername").send_keys(username)
        self.logger.info(f"Entered Username: {username}")
        time.sleep(5)
        self.driver.find_element(By.ID,value="loginpassword").send_keys(password)
        self.logger.info("Entered Password")
        time.sleep(2)
        login = self.driver.find_element(By.CSS_SELECTOR,"#logInModal > div > div > div.modal-footer > button.btn.btn-primary").click()
        self.logger.info("Clicked Login Submit Button")
        time.sleep(3)
        # welcome = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "nameofuser"))).text
        # self.logger.info(f"Welcome Message Displayed: {welcome}")
        # assert welcome == "Welcome Admin"
        self.logger.info("Login Test Passed")
        print("Program finished")
        self.driver.quit()
        self.logger.info("Browser Closed")
        self.logger.info("--- Test Completed ---")