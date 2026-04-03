import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.search_page import SearchPage
from elements.elements import *
import allure


@allure.suite("Тестирование поиска в Гугл")
@pytest.mark.google_search_suite
class TestGoogleSearchSuite:
    @allure.title("Поиск в Гугл")
    @pytest.mark.parametrize("is_enter_pressed", (False, True))
    @pytest.mark.google_search
    def test_google_search(self, driver: WebDriver, is_enter_pressed: bool) -> None:
        page = SearchPage(driver)
        element = SearchPageElements()
        page.open()
        page.check_element(element.SEARCH_FIELD)
        page.type_in_element(element.SEARCH_FIELD, "Яндекс")
        page.check_element(element.HINT_LIST)
        with allure.step("Проверить, что в списке подсказок есть слово 'яндекс' (не в рекламном блоке)"):
            hints = "\n".join(page.get_elements_attribute(element.HINT_LIST_ITEM, start_index=1))
            allure.attach(hints, attachment_type=allure.attachment_type.TEXT)
            assert "яндекс" in hints, "Слова 'яндекс' нет в списке подсказок"
        page.execute_search(is_enter_pressed)
        with allure.step("Проверить, что в первых 5 результатах поиска есть ссылка на yandex.ru"):
            sites = "\n".join(page.get_elements_attribute(element.RESULTS_TABLE_ITEM_SITE, end_index=5))
            allure.attach(sites, attachment_type=allure.attachment_type.TEXT)
            assert "yandex.ru" in sites, "Домен yandex.ru отсутствует среди первых пяти результатов"

    @allure.title("Картинки в Гугл")
    @pytest.mark.pictures_in_google
    def test_pictures_in_google(self, driver: WebDriver) -> None:
        self.test_google_search(driver, False)
        page = SearchPage(driver)
        element = SearchPageElements()
        page.check_element(element.PICTURES_BUTTON)
        page.click_on_element(element.PICTURES_BUTTON)
        with allure.step("Открыть вторую картинку, проверить, что она открылась"):
            page.check_element(element.PICTURE_ITEM)
            page.click_on_element(element.PICTURE_ITEM)
            page.check_element(element.SELECTED_PICTURE)
            page.are_pictures_the_same(page.get_element_attribute(element.PICTURE_ITEM, "alt"),
                                       page.get_element_attribute(element.SELECTED_PICTURE, "alt"))
            second_picture_src = page.get_element_attribute(element.SELECTED_PICTURE, "src")
        with allure.step("При нажатии кнопки 'Следующее изображение' картинка должна измениться"):
            page.check_element(element.NEXT_PICTURE_BUTTON)
            page.click_on_element(element.NEXT_PICTURE_BUTTON)
            page.check_element(element.SELECTED_PICTURE)
            page.is_picture_changed(element.SELECTED_PICTURE, second_picture_src)
        page.check_element(element.PREVIOUS_PICTURE_BUTTON)
        page.click_on_element(element.PREVIOUS_PICTURE_BUTTON)
        with allure.step("Проверить, что картинка изменилась на картинку из шага 4"):
            page.check_element(element.SELECTED_PICTURE)
            page.are_pictures_the_same(page.get_element_attribute(element.SELECTED_PICTURE, "src"),
                                       second_picture_src)
