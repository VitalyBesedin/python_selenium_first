
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# g = Service()
# driver = webdriver.Chrome(options=options, service=g)  # this is and above macOS
driver = webdriver.Chrome()  # Windows
# driver = webdriver.Firefox()
# driver = webdriver.Safari()

base_url = 'https://html5css.ru/howto/howto_js_rangeslider.php'
driver.get(base_url)
driver.maximize_window()
time.sleep(5)
action = ActionChains(driver)

# move = driver.find_element(By.CSS_SELECTOR, "#id2")
move = driver.find_element(By.XPATH, "//*[@id='slidecontainer']/input")
action.click_and_hold(move).move_by_offset(50, 0).release().perform()
print("Move +")

time.sleep(5)
