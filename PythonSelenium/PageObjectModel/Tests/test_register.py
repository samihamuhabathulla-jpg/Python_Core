import pytest
from Pages.RegisterPage import RegisterPage
from Utilities import read_config
import Utilities.logCreator

@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister:

    logger = Utilities.logCreator.log_creator()
    def test_register_existing_email(self):

        firstname = read_config.get_data("Register Data","firstname")
        lastname = read_config.get_data("Register Data","lastname")
        email = read_config.get_data("Register Data","email")
        telephone = read_config.get_data("Register Data","telephone")
        password = read_config.get_data("Register Data","password")
        register = RegisterPage(self.driver)

        register.click_dropdown()
        self.logger.info("Dropdown clicked")

        register.click_register_link()
        self.logger.info("Register link clicked")

        register.enter_firstname(firstname)
        register.enter_lastname(lastname)
        register.enter_email(email)
        register.enter_telephone(telephone)
        register.enter_password(password)
        register.enter_confirm_password(password)

        self.logger.info("Registration details entered")

        register.click_privacy_policy()

        register.click_continue_button()
        expected = "Warning: E-Mail Address is already registered!"
        actual = register.get_warning_message()
        assert expected in actual
        self.logger.info("Warning message displayed successfully")