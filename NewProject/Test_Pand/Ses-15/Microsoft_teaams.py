from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from pynput.keyboard import Key, Controller
serv_obj=Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options)
import time
driver.get("https://www.google.co.in/")
driver.maximize_window()
driver.implicitly_wait(10)


# keyboard=Controller()
# keyboard.press(Key.shift)
# keyboard.
# keyboard.release(Key.shift)

act=ActionChains(driver)

for i in range(20):
    act.send_keys("a").perform()
    time.sleep(8)
    act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
    time.sleep(8)
    act.key_down(Keys.CONTROL).send_keys("x").key_up(Keys.CONTROL).perform()
    driver.refresh()
    time.sleep(10)
    print("Hi")

