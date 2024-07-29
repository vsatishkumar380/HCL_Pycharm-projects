import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

serv_obj=Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options)
driver.implicitly_wait(10)

driver.get("https://plupload.com/examples/")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[@id='uploader_browse']").click()
time.sleep(3)

keyboard=Controller()
keyboard.type("C:\\Users\\svankada\\Pictures\\cancel.PNG")
time.sleep(3)
keyboard.press(Key.enter)
keyboard.release(Key.enter)


