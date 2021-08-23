from selenium.webdriver.common.by import By
from utilities.baseClass import BaseClass
from pageObjects.SeasonPage import SeasonPage


class HomePage(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    season_links = (By.CSS_SELECTOR, "[href*='season']")
    rpdr_seasons_header = (By.XPATH, "//h3[contains(text(),'RPDR Seasons')]")
    rpdr_as_seasons_header = (By.XPATH, "//h3[contains(text(),'All Stars Seasons')]")

    def get_season_links(self):
        links = self.driver.find_elements(*HomePage.season_links)
        return links

    def get_seasons_header(self):
        return self.driver.find_element(*HomePage.rpdr_seasons_header)

    def get_as_seasons_header(self):
        return self.driver.find_element(*HomePage.rpdr_as_seasons_header)

    def choose_season(self):
        links = self.get_season_links()
        self.choose_random_link(links).click()
        season_page = SeasonPage(self.driver)

        return season_page
