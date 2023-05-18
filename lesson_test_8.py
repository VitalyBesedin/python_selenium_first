import datetime
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# g = Service()
# driver = webdriver.Chrome(options=options, service=g)  # this is and above macOS
driver = webdriver.Chrome()  # Windows
# driver = webdriver.Firefox()
# driver = webdriver.Safari()
# driver = webdriver.Edge()
base_url = 'https://demoqa.com/checkbox'
driver.get(base_url)
driver.maximize_window()


check_box = driver.find_element(By.XPATH, "//span[@class='rct-checkbox']")
check_box.click()
time.sleep(5)
check_box_1 = driver.find_element(By.XPATH, "//button[@aria-label='Toggle']")
check_box_1.click()










time.sleep(5)
