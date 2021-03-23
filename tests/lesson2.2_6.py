import time
import math
from selenium.webdriver.common.by import By
from selenium import webdriver


def ln(value_x):
    return str(math.log(abs(12 * math.sin(value_x))))


try:
    browser = webdriver.Chrome()
    link = 'http://SunInJuly.github.io/execute_script.html'
    browser.get(link)
    data_value = browser.find_element(By.ID, 'input_value')
    data_value = int(data_value.text)
    data_answer = ln(data_value)
    data_input = browser.find_element(By.ID, 'answer').send_keys(data_answer)
    checkbox = browser.find_element(By.ID, "robotCheckbox").click()
    radiobutton = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()
    submit = browser.find_element(By.CSS_SELECTOR, 'data_price.btn')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()


finally:
    time.sleep(5)
    browser.quit()
