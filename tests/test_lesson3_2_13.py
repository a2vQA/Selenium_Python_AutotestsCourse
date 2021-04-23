from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()


class Test3_2_13(unittest.TestCase):
    def test_true1(self):
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
        Submit = browser.find_element(By.CSS_SELECTOR, ".btn")
        Submit.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1").text
        self.assertEqual(welcome_text_elt, "Congratulations! You have successfully registered!")


    def test_true2(self):
        browser = webdriver.Chrome()
        browser.get(link2)
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
        Submit = browser.find_element(By.CSS_SELECTOR, ".btn")
        Submit.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1").text
        self.assertEqual(welcome_text_elt, "Congratulations! You have successfully registered!")


if __name__ == "__main__": unittest.main()
time.sleep(7)
browser.quit()
