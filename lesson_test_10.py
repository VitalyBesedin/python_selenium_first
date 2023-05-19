import datetime
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# g = Service()
# driver = webdriver.Chrome(options=options, service=g)  # this is and above macOS
# driver = webdriver.Chrome()  # Windows
# driver = webdriver.Firefox()
driver = webdriver.Safari()
# driver = webdriver.Edge()
base_url = 'https://testpages.herokuapp.com/styled/basic-html-form-test.html'
driver.get(base_url)
driver.maximize_window()

time.sleep(2)
check_box = driver.find_element(By.XPATH, "//input[@value='cb1']")
check_box.click()
time.sleep(2)
check_box_1 = driver.find_element(By.XPATH, "//input[@value='cb3']")
check_box_1.click()
time.sleep(2)
radio_button = driver.find_element(By.XPATH, "//input[@value='rd1']")
radio_button.click()

time.sleep(5)
