import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    FN = browser.find_element(By.CSS_SELECTOR, '[placeholder = "Enter first name"]').send_keys('kek')
    LN = browser.find_element(By.CSS_SELECTOR, '[placeholder = "Enter last name"]').send_keys('krek')
    Email = browser.find_element(By.CSS_SELECTOR, '[placeholder = "Enter email"]').send_keys('kek@mail.ru')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file_example.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.ID, 'file').send_keys(file_path)
    submit = browser.find_element(By.CSS_SELECTOR, 'data_price.btn').click()

finally:
    time.sleep(5)
    browser.quit()
