import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import math

browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/get_attribute.html"

    browser.get(link)
    treasure = browser.find_element(By.ID, "treasure")
    treasure_value = treasure.get_attribute("valuex")


    def calc(treasure_value):
        return str(math.log(abs(12 * math.sin(int(treasure_value)))))

    y = calc(treasure_value)
    data_input = browser.find_element(By.ID, "answer")
    data_input.send_keys(y)
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()
    data_submit = browser.find_element(By.CSS_SELECTOR, "data_price.btn")
    data_submit.click()
    time.sleep(5)

finally:
    browser.quit()
