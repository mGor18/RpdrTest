from pageObjects.QueenPage import QueenPage
from utilities.baseClass import BaseClass
from selenium.webdriver.common.by import By


class SeasonPage(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    contestant_links = (By.CSS_SELECTOR, "[href*='queen']")
    contestants_header = (By.XPATH, "//h3[text()[contains(.,'Contestants')]]")
    seasons_header = (By.XPATH, "//h3[text()[contains(.,'Seasons')]]")
    episode_names = (By.XPATH, "//div[text()[contains(., 'Episode')]]")

    def get_contestant_links(self):
        return self.driver.find_elements(*SeasonPage.contestant_links)

    def get_contestants_header(self):
        return self.driver.find_element(*SeasonPage.contestants_header)

    def get_seasons_header(self):
        return self.driver.find_element(*SeasonPage.seasons_header)

    def get_episodes(self):
        return self.driver.find_elements(*SeasonPage.episode_names)

    def choose_contestant(self):
        links = self.get_contestant_links()
        self.choose_random_link(links).click()
        queen_page = QueenPage(self.driver)

        return queen_page
