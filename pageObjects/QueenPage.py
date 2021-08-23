from selenium.webdriver.common.by import By


class QueenPage:
    def __init__(self, driver):
        self.driver = driver

    header_link = (By.TAG_NAME, ".header-container")
    queen_image = (By.CSS_SELECTOR, "[class='contestant-image']")
    info_box = (By.CLASS_NAME, "[class='info-container']")

    def get_header(self):
        return self.driver.find_element(*QueenPage.header_link)

    def get_queen_image(self):
        return self.driver.find_element(*QueenPage.queen_image)

    def get_info_box(self):
        return self.driver.find_element(*QueenPage.info_box)
