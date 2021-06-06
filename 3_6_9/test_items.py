import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def test_basket_exists_on_page(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(10)
    assert browser.find_elements(By.CLASS_NAME, 'btn-add-to-basket'), 'Кнопка добавления в корзину отсутствует на странице'
