import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)

# driver = webdriver.Firefox()
# driver = webdriver.Safari()
# driver = webdriver.Edge()
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()
# username = driver.find_element_by_id("user-name")
# username = driver.find_element(by=By.ID, value="user-name")
# username = driver.find_element(By.ID, "user-name")  # ID
# username = driver.find_element(By.NAME, "user-name")    # NAME
# username = driver.find_element(By.XPATH, "//*[@id='user-name']")    # Full XPATH
# username = driver.find_element(By.XPATH, "//input[@id='user-name']")    # ID XPATH
username = driver.find_element(By.XPATH, "//input[@data-test='username']")    # data-test XPATH
username.send_keys('standard_user')
# password = driver.find_element(By.XPATH, "//*[@id='password']")    # Full XPATH
password = driver.find_element(By.CSS_SELECTOR, "#password")    # CSS_SELECTOR
password.send_keys('secret_sauce')
button_login = driver.find_element(By.XPATH, "//input[@value='Login']")
button_login.click()


time.sleep(5)
# driver.close()

# id
# name
# class_name
# xpath
# link_text
# tag_name
# css_selector
