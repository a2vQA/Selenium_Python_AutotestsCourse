from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://megafon-dev.vpool"
data_email = "v.artyomenko@qsoft.ru"
data_login = "testirovanie"
data_password = "qwerty78"


def auth():
    login = browser.find_element(By.ID, "login")
    login.send_keys(x)
    password = browser.find_element(By.ID, "password")
    password.send_keys(data_password)
    button = browser.find_element(By.CLASS_NAME, "button__text")
    button.click()
    time.sleep(2)


try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = data_email
    auth()
    browser.delete_all_cookies()
    browser.refresh()
    x = data_login
    auth()


finally:
    time.sleep(2)
    browser.quit()
