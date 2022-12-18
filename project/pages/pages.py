import time
from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import exceptions
from datetime import datetime


class BasePage:

    def __init__(self, driver: Chrome):
        self.browser = driver

    def click(self, obj):
        if self.is_element_present(obj):
            self.browser.find_element(*obj).click()
            time.sleep(0.5)

    def clear_field(self, field):
        self.browser.find_element(*field).clear()

    def get_element_text(self, obj):
        text = self.browser.find_element(*obj).text
        return text

    def get_element_attribute_value(self, obj, attr):
        val = self.browser.find_element(*obj).get_attribute(attr)
        return val

    def is_element_present(self, obj):
        try:
            self.browser.find_element(*obj)
        except NoSuchElementException:
            return False
        return True

    def is_element_visible(self, obj):
        try:
            self.browser.find_element(*obj).is_displayed()
        except NoSuchElementException:
            return False
        return True

    def make_screenshot(self):
        now = datetime.now()
        name = now.strftime('screenshot_' + '%Y-%m-%d_%H-%M-%S' + '.png')
        self.browser.save_screenshot('project/screen/' + name)

    def mouse_move_to_element(self, locator):
        actions = ActionChains(self.browser)
        obj = self.browser.find_element(*locator)
        actions.move_to_element(obj)
        actions.perform()
        time.sleep(0.5)

    def open(self, url):
        self.browser.get(url)

    def type_text(self, obj, val):
        self.clear_field(obj)
        self.browser.find_element(*obj).send_keys(val)

    def wait_for_element_is_present(self, obj, timeout):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(obj))
        except exceptions.TimeoutException:
            pass


class BasketPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        assert self.browser.current_url.endswith('/basket/'), "Переход на страницу корзины не выполнен"