import time
from selenium import webdriver
from selenium.webdriver import Keys
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

login_standard_user = "standard_user"
password_all = "secret_sauce"

username = driver.find_element(By.XPATH, "//input[@data-test='username']")
username.send_keys(login_standard_user)
print("Input login")
password = driver.find_element(By.CSS_SELECTOR, "#password")
password.send_keys(password_all)
print("Input password")
password.send_keys(Keys.RETURN)

filt_r = driver.find_element(By.XPATH, "//select[@data-test='product_sort_container']")
filt_r.click()
print("Click Filter")
time.sleep(5)
filt_r.send_keys(Keys.DOWN)
time.sleep(5)
filt_r.send_keys(Keys.RETURN)

# time.sleep(2)
# username.send_keys(Keys.BACKSPACE)
# time.sleep(2)
# username.send_keys(Keys.BACKSPACE)
# time.sleep(2)
# username.send_keys('er')
# password = driver.find_element(By.CSS_SELECTOR, "#password")
# password.send_keys(password_all)
# print("Input password")
# button_login = driver.find_element(By.XPATH, "//input[@value='Login']")
# button_login.click()
# print("Click login button")



time.sleep(5)
