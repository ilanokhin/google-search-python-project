from locators.locator_utils import locator


class BasePageLocators:
    LOGIN_BUTTON = locator(".gb_A")


class SearchPageLocators(BasePageLocators):
    SEARCH_FIELD = locator("//textarea[@id='APjFqb']")
    HINT_LIST = locator(".erkvQe>div>ul")
    HINT_LIST_ITEM = locator(".erkvQe>div>ul>li")
    SEARCH_BUTTON = locator("input[name=btnK]")
    RESULTS_TABLE = locator("#search")
    RESULTS_TABLE_ITEM_SITE = locator("#search a cite")
    PICTURES_BUTTON = locator("//span[contains(text(),'Картинки')]")
    PICTURE_ITEM = locator("//div[@jscontroller='XW992c']/div[2]//img[string-length(@alt)>0]")
    SELECTED_PICTURE = locator("//div[@aria-hidden='false']//div[@aria-hidden='false']//img[@jsname='JuXqh']")
    NEXT_PICTURE_BUTTON = locator("//div[@data-sci='1']//button[@aria-label='Следующее изображение']")
    PREVIOUS_PICTURE_BUTTON = locator("//div[@data-sci='2']//button[@aria-label='Предыдущее изображение']")
