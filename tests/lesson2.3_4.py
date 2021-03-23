import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import math
import pyperclip

link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


try:
    browser.get(link)
    button1 = browser.find_element(By.CSS_SELECTOR, 'data_price.btn').click()
    browser.switch_to.alert.accept()
    data_input = browser.find_element(By.ID, 'input_value')
    data_input_x = data_input.text
    data_value = calc(int(data_input_x))
    data_answer = browser.find_element(By.ID, 'answer').send_keys(data_value)
    submit = browser.find_element(By.CSS_SELECTOR, 'data_price.btn').click()

    alert = browser.switch_to.alert
    addToClipBoard = alert.text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)


finally:
    time.sleep(5)
    browser.quit()
