import pytest
from Pages.LogoutPage import LogoutPage
from Utilities import read_config
import Utilities.logCreator

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogout:
    logger = Utilities.logCreator.log_creator()
    def test_logout(self):
        email = read_config.get_data("Login credentials","email")
        password = read_config.get_data("Login credentials","password")
        logout = LogoutPage(self.driver)

        logout.click_dropdown()
        self.logger.info("Dropdown clicked")

        logout.click_login()

        logout.enter_email(email)
        self.logger.info("Email entered")

        logout.enter_password(password)
        self.logger.info("Password entered")

        logout.click_login_button()
        self.logger.info("Login successful")

        logout.click_my_account()
        self.logger.info("My Account clicked")

        logout.click_logout()
        self.logger.info("Logout clicked")

        assert logout.verify_logout()
        self.logger.info("Logout successful")