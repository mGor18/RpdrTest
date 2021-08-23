import pytest
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.mark.usefixtures("setup_driver")
class BaseClass:
    driver = None
    home_page = None
    season_page = None

    def choose_random_link(self, links):
        elements = links
        max_num = len(elements) - 1

        random_link = elements[random.randrange(1, max_num)]

        print(random_link)
        return random_link

    # def verify_page_loaded(self, locator, element):
    #    WebDriverWait(self.driver, 10).until(
    #        ec.presence_of_element_located((locator, element)))

    #    assert element.is_displayed()

    def verify_page_loaded(self, text, input_text):
        assert text == input_text
