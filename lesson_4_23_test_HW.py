import datetime
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

def days_in_a_month(month): # calculate days in a month
    if month == 2:
        return 28
    elif month in [4,6,9,11]:
        return 30
    else:
        return 31

driver = webdriver.Chrome()
base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
driver.maximize_window()

new_date = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
new_date.click()
now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d")
print(now_date)
now_date_day = now_date[-2:]
print(now_date_day)
now_date_month = now_date[5:7]
print(now_date_month)
now_date_year = now_date[:4]
print(now_date_year)

if int(now_date_day) + 10 > days_in_a_month(int(now_date_month)):
    day_plus_10 = int(now_date_day) + 10 - days_in_a_month(int(now_date_month))
    actual_month = int(now_date_month) + 1
else:
    day_plus_10 = int(now_date_day) + 10
    actual_month = int(now_date_month)

if day_plus_10 < 10:
    day = "0" + str(day_plus_10)
else:
    day = str(day_plus_10)
if actual_month < 10:
    month = "0" + str(actual_month)
else:
    month = str(actual_month)

for _ in range(10):
    new_date.send_keys(Keys.BACKSPACE)

date_plus_10 = month+"/"+day+"/"+now_date_year
print(date_plus_10)
new_date.send_keys(date_plus_10)
new_date.send_keys(Keys.RETURN)

time.sleep(10)
