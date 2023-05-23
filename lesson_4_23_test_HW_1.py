import datetime
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
driver.maximize_window()

new_date = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
new_date.click()
"""parsing the current date"""
now_date = datetime.date.today()

"""creating the date + 10"""
date_plus_10 = str(datetime.datetime.today() + datetime.timedelta(days=10))


for _ in range(10): # clearing date fild
    new_date.send_keys(Keys.BACKSPACE)


new_date.send_keys(date_plus_10)
new_date.send_keys(Keys.RETURN)

time.sleep(10)
