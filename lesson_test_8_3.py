import datetime
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# g = Service()
# driver = webdriver.Chrome(options=options, service=g)  # this is and above macOS
driver = webdriver.Chrome()  # Windows
# driver = webdriver.Firefox()
# driver = webdriver.Safari()
# driver = webdriver.Edge()
base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
driver.maximize_window()

new_date = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
new_date.click()
now_date = datetime.datetime.utcnow().strftime("%d")
print(now_date)
date = int(now_date) + 1
locator = "//div[@aria-label='Choose Tuesday, May " + str(date) + "rd, 2023']"
print(locator)

time.sleep(3)
date_23 = driver.find_element(By.XPATH, locator)
# date_23 = driver.find_element(By.XPATH, "//div[@aria-label='Choose Tuesday, May 23rd, 2023']")
date_23.click()
# new_date.clear()
# for _ in range(10):
#     new_date.send_keys(Keys.BACKSPACE)
# time.sleep(3)
# new_date.send_keys("03/13/2023")
# time.sleep(3)
# new_date.send_keys(Keys.RETURN)

time.sleep(10)
