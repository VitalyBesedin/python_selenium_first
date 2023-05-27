import datetime
import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)  # this is and above macOS
# driver = webdriver.Chrome()  # Windows
# driver = webdriver.Firefox()
# driver = webdriver.Safari()
# driver = webdriver.Edge()
base_url = 'https://demoqa.com/radio-button'
driver.get(base_url)
driver.maximize_window()


# try:
#     visible_button = driver.find_element(By.CSS_SELECTOR, "#visibleAfter")
#     visible_button.click()
# except NoSuchElementException as exception:
#     print("NoSuchElementException exception")
#     time.sleep(7)
#     visible_button = driver.find_element(By.CSS_SELECTOR, "#visibleAfter")
#     visible_button.click()
#     print("Click Visible Button")

yes_checkbox = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
yes_checkbox.click()
try:
    message = driver.find_element(By.XPATH, "//span[@class='text-success']")
    value_message = message.text
    print(value_message)
    assert value_message == 'No'
    print('checkbox No')
except AssertionError as exception:
    driver.refresh()
    yes_checkbox = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
    yes_checkbox.click()
    message = driver.find_element(By.XPATH, "//span[@class='text-success']")
    value_message = message.text
    print(value_message)
    assert value_message == 'Yes'
    print('checkbox Yes')
print('test over')


# time.sleep(10)
