from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import re


class Element:
    def __init__(self, driver: WebDriver, locator: tuple[str, str], timeout: int = 3) -> None:
        self.driver = driver
        self.locator = locator
        self.driver.implicitly_wait(timeout)
        self._wait = WebDriverWait(self.driver, timeout)
        self._elements = self.driver.find_elements(*self.locator)
        self._size = len(self._elements)

    def __repr__(self) -> str:
        return f"\nЭлемент(локатор: '{self.locator[1]}', количество: {self._size})"

    def __len__(self) -> int:
        return self._size

    def is_present(self) -> bool:
        return bool(self._elements)

    def is_clickable(self) -> bool:
        return self.is_present() and self._elements[0].is_enabled()

    def is_not_clickable(self) -> bool:
        return self.is_present() and not self._elements[0].is_enabled()

    def is_not_present(self) -> bool:
        return not self._elements

    def type_text(self, text) -> None:
        self._elements[0].send_keys(text)

    def click(self) -> None:
        self._elements[0].click()

    def attribute_values(self, attribute: str = "") -> list:
        if not attribute:
            attribute_values = [element.text for element in self._elements]
        else:
            attribute_values = []
            for element in self._elements:
                attribute_value = element.get_attribute(attribute)
                attribute_value = re.sub(r'<.*?>', '', attribute_value)
                attribute_values.append(attribute_value)
        return attribute_values

    def press(self, keys_to_press: Keys | str) -> None:
        self._elements[0].send_keys(str(keys_to_press))

    def attribute(self, attribute: str = "") -> str:
        if not attribute:
            attribute_value = self._elements[0].text
        else:
            attribute_value = self._elements[0].get_attribute(attribute)
            attribute_value = re.sub(r'<.*?>', '', attribute_value)
        return attribute_value

    def is_attribute_changed(self, attribute: str, old_value: str) -> bool:
        try:
            self._wait.until(ec.none_of(
                ec.text_to_be_present_in_element_attribute(self.locator, attribute, old_value)))
        except TimeoutException:
            return False
        return True
