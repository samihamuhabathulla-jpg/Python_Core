import pytest
from Pages.LoginPage import LoginPage
from Utilities import read_config
import Utilities.logCreator

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:

    logger = Utilities.logCreator.log_creator()
    def test_validLogin(self):

        email = read_config.get_data("Login credentials","email")
        password = read_config.get_data("Login credentials","password")
        login = LoginPage(self.driver)

        login.click_dropdown()
        self.logger.info("Dropdown clicked")

        login.click_login_link()
        self.logger.info("Login link clicked")

        login.enter_email(email)
        self.logger.info("Email entered")

        login.enter_password(password)
        self.logger.info("Password entered")

        login.click_login_button()
        self.logger.info("Login button clicked")

        assert login.verify_login()
        self.logger.info("Login successful")