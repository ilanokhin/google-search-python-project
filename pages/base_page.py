from elements.element import Element
import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver: WebDriver, url: str) -> None:
        self.driver = driver
        self.url = url

    def open(self, url: str = "") -> None:
        if url:
            link = url
        else:
            link = self.url
        with allure.step(f"Перейти по адресу {link}"):
            self.driver.get(link)

    def screenshot(self, screenshot_path: str = "") -> bytes:
        if screenshot_path:
            self.driver.save_screenshot(screenshot_path)
        return self.driver.get_screenshot_as_png()

    def check_element(self, element_data: tuple, is_present: bool = True, is_clickable: bool | None = True,
                      make_screenshot: bool = True) -> bool:
        element = Element(self.driver, element_data[1])
        allure_step = f"Проверить элемент '{element_data[0]}' на "
        assert_error = f"Элемент '{element_data[0]}' "
        if not is_present:
            allure_step += "отсутствие"
            result = element.is_not_present()
            assert_error += "присутствует"
        elif is_present and is_clickable is False:
            allure_step += "некликабельность"
            result = element.is_not_clickable()
            assert_error += "кликабельный"
        elif is_present and is_clickable is None:
            allure_step += "наличие"
            result = element.is_present()
            assert_error += "отсутствует"
        else:
            allure_step += "наличие и кликабельность"
            result = element.is_clickable()
            assert_error += "некликабельный или отсутствует"
        with allure.step(allure_step):
            if make_screenshot:
                allure.attach(self.screenshot(), attachment_type=allure.attachment_type.PNG)
            assert result, assert_error
        return result

    def type_in_element(self, element_data: tuple, text: str) -> None:
        element = Element(self.driver, element_data[1])
        with allure.step(f" Ввести текст '{text}' в элемент '{element_data[0]}'"):
            element.type_text(text)

    def click_on_element(self, element_data: tuple) -> None:
        element = Element(self.driver, element_data[1])
        with allure.step(f" Кликнуть по элементу '{element_data[0]}'"):
            element.click()

    def press_keys(self, element_data: tuple, keys: Keys | str = Keys.RETURN, keys_name: str = "ENTER") -> None:
        element = Element(self.driver, element_data[1])
        with allure.step(f" Нажать {keys_name} на элементе '{element_data[0]}'"):
            element.press(keys)

    def get_elements_attribute(self, element_data: tuple, attribute: str = "", start_index: int = 0,
                               end_index: int | None = None) -> list:
        element = Element(self.driver, element_data[1])
        attribute_list = element.attribute_values(attribute)
        finish_index = len(attribute_list) if end_index is None else end_index
        attribute_list = [value for i, value in enumerate(attribute_list) if start_index <= i < finish_index]
        return attribute_list

    def get_element_attribute(self, element_data: tuple, attribute: str = ""):
        element = Element(self.driver, element_data[1])
        return element.attribute(attribute)
