import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import pyperclip
import math

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/redirect_accept.html'
browser.get(link)


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


try:
    data_button = browser.find_element(By.CSS_SELECTOR, 'data_price.trollface').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    data_x = browser.find_element(By.ID, 'input_value').text
    data_input = browser.find_element(By.ID, 'answer').send_keys(calc(int(data_x)))
    data_submit = browser.find_element(By.CSS_SELECTOR, 'data_price.btn').click()
    alert = browser.switch_to.alert
    addToClipBoard = alert.text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)

finally:
    time.sleep(5)
    browser.quit()
