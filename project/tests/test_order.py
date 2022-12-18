import time
from project.pages.pages import BasePage, BasketPage
from project.locators.locators import MainPageLocators, FiltersLocators, ProductLocators, BasketLocators, \
    LoginFormLocators

url = 'https://www.chitai-gorod.ru/'


class TestOrder:

    def test_order_item(self, browser):
        page = BasePage(browser)
        page.open(url)
        page.click(MainPageLocators.LINK_BOOKS)
        page.click(MainPageLocators.LINK_LITERATURE)
        page.wait_for_element_is_present(MainPageLocators.BANNER, 30)
        if page.is_element_visible(MainPageLocators.BANNER):
            time.sleep(3)
            page.click(MainPageLocators.BTN_CLOSE)
            page.click(MainPageLocators.LINK_BOOKS)
            page.click(MainPageLocators.LINK_LITERATURE)
        page.click(FiltersLocators.LST_SORTING)
        page.click(FiltersLocators.SORT_YEAR_DESC)
        page.click(FiltersLocators.CKB_AVAILABLE)
        product_id = page.get_element_attribute_value(MainPageLocators.FIRST_FILTERED_ITEM, 'data-product')
        book_name_list = page.get_element_attribute_value(MainPageLocators.FIRST_FILTERED_ITEM, 'data-chg-book-name')
        book_price_list = page.get_element_attribute_value(MainPageLocators.FIRST_FILTERED_ITEM, 'data-productprice')
        page.click(MainPageLocators.FIRST_FILTERED_ITEM)
        book_name_card = page.get_element_text(ProductLocators.TITLE)
        book_price_card = page.get_element_text(ProductLocators.PRICE).replace(' ₽', '')
        assert browser.current_url[:-1].endswith(product_id), "Переход на страницу товара не выполнен"
        assert book_name_list == book_name_card, f"Название товара в каталоге {book_name_list} не соответствует " \
                                                 f"названию товара в карточке {book_name_card}"
        assert book_price_list == book_price_card, f"Цена товара в каталоге {book_price_list} не соответствует " \
                                                   f"цене товара в карточке {book_price_card}"
        assert page.get_element_text(ProductLocators.BTN_BUY) == "Купить", "Проверьте текст кнопки до покупки товара. " \
                                                                           "Ожидаемое значение: Купить"

        page.click(ProductLocators.BTN_BUY)
        time.sleep(1)
        text = page.get_element_text(ProductLocators.BTN_BUY)
        assert text == 'Оформить заказ', "При заказе текст кнопки не сменился. Ожидаемое значение: Оформить заказ"

        page.click(ProductLocators.BTN_BUY)
        page = BasketPage(browser)
        book_name_basket = page.get_element_text(BasketLocators.ITEM_NAME)
        book_price_basket = page.get_element_text(BasketLocators.ITEM_PRICE).replace(' ₽', '')
        total_sum = page.get_element_text(BasketLocators.TOTAL_SUM)
        assert book_name_basket == book_name_card, f"Название товара в карточке {book_name_card} не соответствует " \
                                                   f"названию товара в корзине {book_name_basket}"
        assert book_price_basket == book_price_card, f"Цена товара в карточке {book_price_card} не соответствует " \
                                                     f"цене товара в корзине {book_price_basket}"
        assert total_sum == book_price_basket, "Общая сумма должна быть равна цене одного товара"

        page.click(BasketLocators.BTN_SUBMIT)
        assert page.is_element_visible(LoginFormLocators.DLG_LOGIN)

        tab_text = page.get_element_text(LoginFormLocators.TAB_ACTIVE_DEFAULT)
        assert tab_text == 'Вход', "По умолчанию должен быть выбран таб входа по номеру телефона"

        page.make_screenshot()

        page.click(LoginFormLocators.BTN_CLOSE)

