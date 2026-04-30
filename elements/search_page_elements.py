from elements.base_page_elements import BasePageElements
from utils.universal_locator import locator


class SearchPageElements(BasePageElements):
    SEARCH_FIELD = ("Поле поиска", locator("//textarea[@id='APjFqb']"))
    HINT_LIST = ("Список подсказок", locator(".erkvQe>div>ul"))
    HINT_LIST_ITEM = ("Строчка из списка подсказок", locator(".erkvQe>div>ul>li"))
    SEARCH_BUTTON = ("Кнопка поиска", locator("input[name=btnK]"))
    RESULTS_TABLE = ("Таблица с результатами", locator("#search"))
    RESULTS_TABLE_ITEM_SITE = ("Сайт из таблицы с результатами", locator("#search a cite"))
    PICTURES_BUTTON = ("Картинки", locator("//span[contains(text(),'Картинки')]"))
    PICTURE_ITEM = ("Картинка в поисковой выдаче",
                    locator("//div[@jscontroller='XW992c']/div[2]//img[string-length(@alt)>0]"))
    SELECTED_PICTURE = ("Выбранная картинка",
                        locator("//div[@aria-hidden='false']//div[@aria-hidden='false']//img[@jsname='JuXqh']"))
    NEXT_PICTURE_BUTTON = ("Следующее изображение",
                           locator("//div[@data-sci='1']//button[@aria-label='Следующее изображение']"))
    PREVIOUS_PICTURE_BUTTON = ("Предыдущее изображение",
                               locator("//div[@data-sci='2']//button[@aria-label='Предыдущее изображение']"))
