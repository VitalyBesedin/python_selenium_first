import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# g = Service()
# driver = webdriver.Chrome(options=options, service=g)
# driver = webdriver.Firefox()
driver = webdriver.Safari()
# driver = webdriver.Edge()
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
password_all = "secret_sauc" # negative test

username = driver.find_element(By.XPATH, "//input[@data-test='username']")
username.send_keys(login_standard_user)
print("Input login")
password = driver.find_element(By.CSS_SELECTOR, "#password")
password.send_keys(password_all)
print("Input password")
button_login = driver.find_element(By.XPATH, "//input[@value='Login']")
button_login.click()
print("Click login button")

warring_text = driver.find_element(By.XPATH, "//h3[@data-test='error']")
value_warring_text = warring_text.text
assert value_warring_text == 'Epic sadface: Username and password do not match any user in this service'
print("Good test")

time.sleep(3)
driver.refresh()
time.sleep(5)

