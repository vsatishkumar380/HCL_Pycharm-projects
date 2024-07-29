from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
serv_obj=Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options)

driver.get("https://anotepad.com/")
time.sleep(5)
driver.maximize_window()
driver.get("https://www.snapdeal.com/")
driver.get("https://www.google.co.in/")

for i in range(50):
    time.sleep(5)
    driver.back()
    time.sleep(10)
    driver.forward()
    time.sleep(5)
    driver.refresh()
    time.sleep(5)






