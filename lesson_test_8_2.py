import datetime
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
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
base_url = 'https://demoqa.com/buttons'
driver.get(base_url)
driver.maximize_window()

action = ActionChains(driver)
double = driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
action.double_click(double).perform()





time.sleep(25)
