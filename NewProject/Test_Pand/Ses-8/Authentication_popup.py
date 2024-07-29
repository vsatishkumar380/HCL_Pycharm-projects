from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options)

import time

# Syntax: http://username:password@test.com
# Ex:https://admin:admin@the-internet.herokuapp.com/basic_auth

driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()


