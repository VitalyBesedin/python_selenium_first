import datetime
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
# driver = webdriver.Chrome()
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
time.sleep(5)

# driver.execute_script("window.scrollTo(0, 500)")
action = ActionChains(driver)
# red_tshirt = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']")
red_tshirt = driver.find_element(By.XPATH, "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
action.move_to_element(red_tshirt).perform()

time.sleep(3)
now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
name_screenshot = 'screenshot' + now_date + '.png'
driver.save_screenshot('/Users/vitalybesedin/PycharmProjects/python_selenium_first/screen/' + name_screenshot) # MacOS
# driver.save_screenshot('C:\\Users\\vit\\PycharmProjects\\python_selenium_first\\screen\\' + name_screenshot) # Windows

time.sleep(5)
