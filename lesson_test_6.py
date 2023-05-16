import datetime
import time
from selenium import webdriver
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
button_login = driver.find_element(By.XPATH, "//input[@value='Login']")
button_login.click()
print("Click login button")

"""Info Product # 1"""
product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_product_1 = product_1.text
print(value_product_1)
price_product_1 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
value_price_product_1 = price_product_1.text
print(value_price_product_1)
select_product_1 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
select_product_1.click()
print("Select Product 1")
cart = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
cart.click()
print("Enter Cart")

""" Info Cart Product 1"""
cart_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)
assert value_product_1 == value_cart_product_1
print("Info Cart Product 1 GOOD")
price_cart_product_1 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_cart_price_product_1 = price_cart_product_1.text
print(value_cart_price_product_1)
assert value_price_product_1 == value_cart_price_product_1
print("Info Cart Price Product 1 GOOD")
checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
checkout.click()
print("Click Checkout")

"""Select User Info"""
first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys('Ivan')
print("Input First Name")
last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys('Ivanov')
print("Input Last Name")
zip_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")
zip_code.send_keys('111111')
print("Input ZIP Code")
continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
continue_button.click()
print("Click Continue")

""" Info Order Product 1"""
order_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_order_product_1 = order_product_1.text
print(value_order_product_1)
assert value_product_1 == value_order_product_1
print("Info Order Product 1 GOOD")
price_order_product_1 = driver.find_element(By.XPATH, "//div[@class='inventory_item_price']")
value_order_price_product_1 = price_order_product_1.text
print(value_order_price_product_1)
assert value_price_product_1 == value_order_price_product_1
print("Info Order Price Product 1 GOOD")
summery_price = driver.find_element(By.XPATH, "//div[@class='summary_subtotal_label']")
value_summery_price = summery_price.text
print(value_summery_price)
item_total = 'Item total: ' + value_order_price_product_1
print(item_total)
assert value_summery_price == item_total
print("Total Summery Price GOOD")

finish = driver.find_element(By.XPATH, "//button[@id='finish']")
finish.click()
print("Click Finish")
time.sleep(5)
