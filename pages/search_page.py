from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from elements.search_page_elements import *
import allure


class SearchPage(BasePage):
    def __init__(self, driver: WebDriver, url: str = "https://www.google.com") -> None:
        super().__init__(driver, url)

    @allure.step("Выполнить поиск")
    def execute_search(self, press_enter: bool = False) -> None:
        self.check_element(SearchPageElements.SEARCH_BUTTON)

        if press_enter:
            self.press_keys(SearchPageElements.SEARCH_BUTTON, "ENTER", Keys.ENTER)
        else:
            self.click_on_element(SearchPageElements.SEARCH_BUTTON)

        self.check_element(SearchPageElements.RESULTS_TABLE)

