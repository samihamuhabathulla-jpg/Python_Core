import pytest
from Pages.SearchPage import SearchPage
from Utilities import read_config
import Utilities.logCreator

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    logger = Utilities.logCreator.log_creator()
    def test_validproduct(self):

        product = read_config.get_data("Search Data","product")
        search = SearchPage(self.driver)

        search.enter_product(product)
        self.logger.info("Product entered")

        search.click_search()
        self.logger.info("Search button clicked")

        assert search.product_displayed()

        self.logger.info("Product displayed")