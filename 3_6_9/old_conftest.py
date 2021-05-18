import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language by his ISO code")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    languages = {'ar', 'ca', 'cs', 'da', 'de', 'en-gb', 'el', 'es', 'fi', 'fr', 'it', 'ko', 'nl', 'pl', 'pt',
                 'pt - br', 'ro', 'ru', 'sk', 'uk', 'zh-hans'}
    link = f"http://selenium1py.pythonanywhere.com/{languages}/catalogue/coders-at-work_207/"
    browser = None
    if browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    elif browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
        if language == f"{languages}":
            print(f"\nOpening site with {language} language")
            browser.get(link)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
