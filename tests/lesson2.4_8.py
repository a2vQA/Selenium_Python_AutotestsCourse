import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import math
import pyperclip
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/explicit_wait2.html'
browser.implicitly_wait(5)


try:
    browser.get(link)

    data_book = browser.find_element(By.ID, 'book')
    data_price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    data_book.click()
    data_x = browser.find_element(By.ID, 'input_value').text
    data_input = browser.find_element(By.ID, 'answer').send_keys(calc(int(data_x)))
    data_submit = browser.find_element(By.ID, 'solve')
    browser.execute_script("return arguments[0].scrollIntoView(true);", data_submit)
    data_submit.click()
    alert = browser.switch_to.alert
    addToClipBoard = alert.text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)

finally:
    time.sleep(13)
    browser.quit()
