from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link1 = "http://suninjuly.github.io/registration1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link1)

    FirstName = browser.find_element(By.CSS_SELECTOR, ".first_block>:nth-child(1)>input")
    FirstName.send_keys("Name")
    LastName = browser.find_element(By.CSS_SELECTOR, ".first_block>:nth-child(2)>input")
    LastName.send_keys("SurName")
    EMail = browser.find_element(By.CSS_SELECTOR, ".first_block>:nth-child(3)>input")
    EMail.send_keys("Email")
    Phone = browser.find_element(By.CSS_SELECTOR, ".second_block>:nth-child(1)>input")
    Phone.send_keys("Number")
    Address = browser.find_element(By.CSS_SELECTOR, ".second_block>:nth-child(2)>input")
    Address.send_keys("Address")
    Submit = browser.find_element(By.CSS_SELECTOR, "data_price.btn")
    Submit.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # alert = browser.switch_to_alert()
    # print(alert.text)
    time.sleep(7)
    browser.quit()
