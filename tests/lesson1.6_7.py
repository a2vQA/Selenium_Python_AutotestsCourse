from selenium import webdriver
from selenium.webdriver.common.by import By
import time
link = "http://suninjuly.github.io/huge_form.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements(By.CSS_SELECTOR, ".first_block input:nth-of-type(1n+1)")
    for element in elements:
        element.send_keys("Test")
    button = browser.find_element_by_css_selector("data_price.btn")
    button.click()
finally:
    alert = browser.switch_to_alert()
    print(alert.text)
    time.sleep(5)
    browser.quit()
