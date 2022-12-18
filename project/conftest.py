import pytest
from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FFOptions


options_chrome = ChromeOptions()
options_chrome.add_argument('--disable-notifications')
#options.add_argument('--headless')

options_ff = FFOptions()
options_ff.set_preference("dom.push.enabled", False)
options_ff.set_preference("dom.webnotifications.enabled", False)

@pytest.fixture()
def browser():
    driver = Chrome(options=options_chrome)
    #driver = Firefox(options=options_ff)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()
