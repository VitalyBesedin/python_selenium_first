import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

"""Functions"""

def add_products_to_cart(number):
    product = driver.find_element(By.CSS_SELECTOR, products[number - 1])
    value_product = product.text
    price_product = driver.find_element(By.XPATH, product_prices[number - 1])
    value_price_product = price_product.text
    select_product = driver.find_element(By.XPATH, select_products[number - 1])
    select_product.click()
    print("Select Product")
    return value_product, value_price_product

def check_product_in_cart(number, value_product, value_price_product):
    cart_product = driver.find_element(By.CSS_SELECTOR, products[number - 1])
    value_cart_product = cart_product.text
    print(value_cart_product)
    assert value_product == value_cart_product
    print("Info Cart Product GOOD")
    price_cart_product = driver.find_element(By.XPATH, price_cart_products)
    value_cart_price_product = price_cart_product.text
    print(value_cart_price_product)
    assert value_price_product == value_cart_price_product
    print("Info Cart Price Product GOOD")

def check_products_in_order(number, value_product, value_price_product):
    order_product = driver.find_element(By.CSS_SELECTOR, products[number - 1])
    value_order_product = order_product.text
    print(value_order_product)
    assert value_product == value_order_product
    print("Info Order Product GOOD")
    price_order_product = driver.find_element(By.XPATH, price_order_products)
    value_order_price_product = price_order_product.text
    print(value_order_price_product)
    assert value_price_product == value_order_price_product
    print("Info Order Price Product GOOD")
    return value_order_price_product

# def is_valid(s):
#     if not s.isdigit():
#         return s.isdigit()
#     elif float(s) % 1 > 0:
#         return False
#     else:
#         return 1 <= int(s) <= 6


products = ["#item_4_title_link", "#item_0_title_link", "#item_1_title_link", "#item_5_title_link", "#item_2_title_link", "#item_3_title_link"]
product_prices = ["//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div", "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div", "//*[@id='inventory_container']/div/div[3]/div[2]/div[2]/div", "//*[@id='inventory_container']/div/div[4]/div[2]/div[2]/div", "//*[@id='inventory_container']/div/div[5]/div[2]/div[2]/div", "//*[@id='inventory_container']/div/div[6]/div[2]/div[2]/div"]
select_products = ["//button[@id='add-to-cart-sauce-labs-backpack']", "//button[@id='add-to-cart-sauce-labs-bike-light']", "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']", "//button[@id='add-to-cart-sauce-labs-fleece-jacket']", "//button[@id='add-to-cart-sauce-labs-onesie']", "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"]
price_cart_products = "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div"
price_order_products = "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div"


print("Приветствую тебя в нашем интернет магазине")
print("Выбери один из следующих товаров и укажи его номер: 1 - Sauce Labs Backpack, 2 - Sauce Labs Bike Light,")
print("3 - Sauce Labs Bolt T-Shirt, 4 - Sauce Labs Fleece Jacket, 5 - Sauce Labs Onesie, 6 - Test.allTheThings() T-Shirt (Red)")
try:
    product = int(input())
except ValueError as exception:
    product = int(input("Введите пожалуйста только целое число от 1-го до 6-ти:"))

# IndexError
# product_number = input()
# print(product_number)
# while not is_valid(product_number):
#     product_number = input("Введите пожалуйста только целое число от 1-го до 6-ти:")
#     print(product_number)
#
# product = int(product_number)
print(product)
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# g = Service()
# driver = webdriver.Chrome(options=options, service=g)  # this is and above macOS
# driver = webdriver.Chrome()  # Windows
# driver = webdriver.Firefox()
driver = webdriver.Safari()
# driver = webdriver.Edge()
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()
login_standard_user = "standard_user"
password_all = "secret_sauce"



"""Start Test"""
print("Start Test")
username = driver.find_element(By.XPATH, "//input[@data-test='username']")
username.send_keys(login_standard_user)
print("Input login")
password = driver.find_element(By.CSS_SELECTOR, "#password")
password.send_keys(password_all)
print("Input password")
button_login = driver.find_element(By.XPATH, "//input[@value='Login']")
button_login.click()
print("Click login button")

"""Info Products"""
value_product, value_price_product = add_products_to_cart(product)
print(value_product)
print(value_price_product)
cart = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
cart.click()
print("Enter Cart")

""" Info Cart Products"""
check_product_in_cart(product, value_product, value_price_product)
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

""" Info Order Products"""
order_price_product = check_products_in_order(product, value_product, value_price_product)
summery_price = driver.find_element(By.XPATH, "//div[@class='summary_subtotal_label']")
value_summery_price = summery_price.text
print(value_summery_price)

print("End Test")
# """Finishing order"""
# finish = driver.find_element(By.XPATH, "//button[@id='finish']")
# finish.click()
# print("Click Finish")
time.sleep(5)

# IndexError: list index out of range
