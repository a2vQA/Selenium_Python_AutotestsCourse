import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    link1 = 'http://suninjuly.github.io/selects1.html'
    link2 = 'http://suninjuly.github.io/selects2.html'
    browser.get(link1)

    num1 = browser.find_element(By.ID, 'num1')
    data_num1 = int(num1.text)
    num2 = browser.find_element(By.ID, 'num2')
    data_num2 = int(num2.text)
    data_answer = data_num1 + data_num2
    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_visible_text(str(data_answer))
    button = browser.find_element(By.CSS_SELECTOR, 'data_price.btn').click()

finally:
    time.sleep(5)
    browser.quit()
