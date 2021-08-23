import pytest
from pageObjects.Homepage import HomePage
from utilities.baseClass import BaseClass


@pytest.mark.usefixtures("setup_home_page")
class TestHomePage(BaseClass):
    def test_home_page_header(self):
        header_links = self.home_page.get_season_links()

        assert len(header_links) > 13, 'Header links loaded'


@pytest.mark.usefixtures("setup_home_page", "setup_season_page")
class TestSeasonPage(BaseClass):

    def test_season_page_contestants(self):
        contestant_links = self.season_page.get_contestant_links()

        assert len(contestant_links) > 5

    def test_season_episodes(self):
        episodes_list = self.season_page.get_episodes()

        assert len(episodes_list) > 5


@pytest.mark.usefixtures("setup_home_page", "setup_season_page", "setup_queen_page")
class TestQueenPage(BaseClass):

    def test_queen_page_image(self):
        queen_pic = self.queen_page.get_queen_image()

        assert queen_pic.is_displayed()

@pytest.fixture(scope="class")
def setup_home_page(request):
    request.cls.home_page = HomePage(request.cls.driver)
    yield


@pytest.fixture(scope="class")
def setup_season_page(request):
    request.cls.season_page = request.cls.home_page.choose_season()
    yield


@pytest.fixture(scope="class")
def setup_queen_page(request):
    request.cls.queen_page = request.cls.season_page.choose_contestant()
    yield
