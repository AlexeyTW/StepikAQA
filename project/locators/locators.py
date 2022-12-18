from selenium.webdriver.common.by import By


class MainPageLocators:
    BANNER = (By.XPATH, "//div[text()='Крутите на удачу!']")  # Баннер, который надо скрыть
    BTN_CLOSE = (By.CSS_SELECTOR, ".popmechanic-main .popmechanic-close")  # Закрыть баннер
    LINK_BOOKS = (By.XPATH, "//b[text()='Книги']")  # Ссылка на книги
    LINK_LITERATURE = (By.CSS_SELECTOR, ".navigation__item>a[href*='khudozhestvennaya_literatura']")  # Жанр
    FIRST_FILTERED_ITEM = (By.CSS_SELECTOR, ".container_cards>div:nth-child(1)")  # Первый товар после фильтрации


class FiltersLocators:
    LST_SORTING = (By.CSS_SELECTOR, ".selectbox")  # Сортировка
    SORT_YEAR_DESC = (By.CSS_SELECTOR, "div[data-sort='year'][data-order='desc']")  # По году по убыванию
    CKB_AVAILABLE = (By.CSS_SELECTOR, ".avaliable")  # Чекбокс "В наличии"


class ProductLocators:
    TITLE = (By.CSS_SELECTOR, ".product__title")  # Заголовок товара
    PRICE = (By.CSS_SELECTOR, ".product__price")  # Цена товара
    BTN_BUY = (By.CSS_SELECTOR, ".trade-container .button_product")  # Кнопка Купить


class BasketLocators:
    ITEM_NAME = (By.CSS_SELECTOR, ".basket-item__wrapper .basket-item__name")  # Название товара в корзине
    ITEM_PRICE = (By.CSS_SELECTOR, ".basket-item__wrapper .basket-item__price-total")  # Цена товара в корзине
    TOTAL_SUM = (By.CSS_SELECTOR, ".js__total_sum")  # Итого сумма
    BTN_SUBMIT = (By.CSS_SELECTOR, ".go-to-order")  # Кнопка Оформить заказ


class LoginFormLocators:
    DLG_LOGIN = (By.CSS_SELECTOR, ".popup-login[data-chg-shown]")  # Диалог логина
    TAB_ACTIVE_DEFAULT = (By.CSS_SELECTOR, ".popup__auth_tab__active")  # Таб авторизации по умолчанию
    BTN_CLOSE = (By.CSS_SELECTOR, ".popup__header_tabs .popup__close")  # Кнопка закрытия диалога
