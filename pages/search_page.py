from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from elements.element import Element
from pages.base_page import BasePage
from elements.elements import *
import allure


class SearchPage(BasePage):
    def __init__(self, driver: WebDriver, url: str = "https://www.google.com") -> None:
        super().__init__(driver, url)

    @allure.step("Выполнить поиск")
    def execute_search(self, press_enter: bool = False) -> None:
        self.check_element(SearchPageElements.SEARCH_BUTTON)
        if press_enter:
            self.press_keys(SearchPageElements.SEARCH_BUTTON, Keys.ENTER, "ENTER")
        else:
            self.click_on_element(SearchPageElements.SEARCH_BUTTON)
        self.check_element(SearchPageElements.RESULTS_TABLE)

    @allure.step("Проверить соответствие картинок")
    def are_pictures_the_same(self, picture1_attribute_value: str, picture2_attribute_value: str,
                              make_screenshot: bool = True) -> bool:
        if make_screenshot:
            allure.attach(self.screenshot(), attachment_type=allure.attachment_type.PNG)
        assert picture1_attribute_value == picture2_attribute_value, "Картинки не соответствуют"
        return picture1_attribute_value == picture2_attribute_value

    @allure.step("Проверить, что картинка изменилась")
    def is_picture_changed(self, picture_data: tuple, old_attribute_value: str, attribute: str = "src",
                           make_screenshot: bool = True) -> bool:
        picture = Element(self.driver, picture_data[1])
        result = picture.is_attribute_changed(attribute, old_attribute_value)
        if make_screenshot:
            allure.attach(self.screenshot(), attachment_type=allure.attachment_type.PNG)
        assert result, "Картинка не изменилась"
        return result
