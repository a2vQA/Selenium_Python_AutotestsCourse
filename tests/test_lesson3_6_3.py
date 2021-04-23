import time
import math
import pytest
from selenium import webdriver

link = [
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
]


@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.mark.parametrize('links', link)
def test_optional_feedback_correct(browser, links):
    browser.get(links)
    browser.implicitly_wait(10)
    urvn = math.log(int(time.time()))
    textarea = browser.find_element_by_css_selector(".textarea")
    textarea.send_keys(str(urvn))
    browser.find_element_by_css_selector('.submit-submission').click()
    correct = browser.find_element_by_css_selector('.smart-hints__hint').text
    assert correct == 'Correct!', f'Error: {correct}'
