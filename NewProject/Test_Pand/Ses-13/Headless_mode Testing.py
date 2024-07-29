
import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import os
location=os.getcwd()

#advan
#Perform the multiple tasks paralley
#Performance will incerase(time save)
#no of testing done with ui and at final round just verify testing, this testing is preferable.

#disadvan
#you cant see/learn the functinoaliety test case


def Headless_Chrome():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
    options = webdriver.ChromeOptions()
    #headless mode
    options.headless=True
    driver = webdriver.Chrome(service=serv_obj, options=options)
    return driver


def Headless_Edge():
    from selenium.webdriver.edge.service import Service
    serv_obj = Service("C:\\Users\\svankada\\Drivers\\msedgedriver.exe")
    options = webdriver.EdgeOptions()
    # headless mode
    options.headless=True
    driver = webdriver.Edge(service=serv_obj, options=options)
    return driver

def hEADLESS_Firefox():
    from selenium.webdriver.firefox.service import Service
    serv_obj = Service("C:\\Users\\svankada\\Drivers\\geckodriver.exe")
    #setting
    ops=webdriver.FirefoxOptions()
    # headless mode
    ops.headless = True
    driver = webdriver.Firefox(service=serv_obj,options=ops)
    return driver


# driver=Headless_Chrome()
driver=Headless_Edge()
driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

print("Title of the page:",driver.title)
print("current url:",driver.current_url)

#driver.close()



