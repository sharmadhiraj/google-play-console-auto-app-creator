from selenium import webdriver

from tasks.login import login

driver = webdriver.Chrome()

try:
    login(driver)

finally:
    driver.quit()
