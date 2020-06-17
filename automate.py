from selenium import webdriver

driver = webdriver.Chrome(executable_path='./drivers/chromedriver')
driver.get('http://www.google.com')