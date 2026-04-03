from locators.locators import BasePageLocators
from locators.locators import SearchPageLocators

class BasePageElements:
    LOGIN_BUTTON = ("Кнопка логина", BasePageLocators.LOGIN_BUTTON)


class SearchPageElements(BasePageElements):
    SEARCH_FIELD = ("Поле поиска", SearchPageLocators.SEARCH_FIELD)
    HINT_LIST = ("Список подсказок", SearchPageLocators.HINT_LIST)
    HINT_LIST_ITEM = ("Строчка из списка подсказок", SearchPageLocators.HINT_LIST_ITEM)
    SEARCH_BUTTON = ("Кнопка поиска", SearchPageLocators.SEARCH_BUTTON)
    RESULTS_TABLE = ("Таблица с результатами", SearchPageLocators.RESULTS_TABLE)
    RESULTS_TABLE_ITEM_SITE = ("Сайт из таблицы с результатами", SearchPageLocators.RESULTS_TABLE_ITEM_SITE)
    PICTURES_BUTTON = ("Картинки", SearchPageLocators.PICTURES_BUTTON)
    PICTURE_ITEM = ("Картинка в поисковой выдаче", SearchPageLocators.PICTURE_ITEM)
    SELECTED_PICTURE = ("Выбранная картинка", SearchPageLocators.SELECTED_PICTURE)
    NEXT_PICTURE_BUTTON = ("Следующее изображение", SearchPageLocators.NEXT_PICTURE_BUTTON)
    PREVIOUS_PICTURE_BUTTON = ("Предыдущее изображение", SearchPageLocators.PREVIOUS_PICTURE_BUTTON)
