import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
# driver = webdriver.Firefox()
#driver = webdriver.Safari()
#driver = webdriver.Edge()
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()
#username = driver.find_element_by_id("user-name")
# username = driver.find_element(by=By.ID, value="user-name")
username = driver.find_element(By.ID, "user-name")
username.send_keys('standard_user')
time.sleep(5)


# time.sleep(5)
# driver.close()

