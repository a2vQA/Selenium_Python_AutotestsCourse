from selenium import webdriver

options = webdriver.FirefoxOptions()
options.binary_location = r"C:\Users\v.artyomenko\AppData\Local\Mozilla Firefox\firefox.exe"
driver = webdriver.Firefox(executable_path=r'C:\geckodriver\geckodriver.exe', options=options)
driver.get('http://inventwithpython.com/')
