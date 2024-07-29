import time
import os

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

driver.get("https://demo.nopcommerce.com/")
#driver.get("https://www.google.co.in/")
driver.maximize_window()

#capture the cookies
cookies=driver.get_cookies()
print("Sizeof cookies",len(cookies)) #3

#print details of all cookies created by browser

# for c in cookies:
#     #print(c)
#     print("name attribute value is",c.get('name'),"   :   ",c.get('value'))


#add a new cookie to browser.
# driver.add_cookie({"name":"mycookie","value":"12345"})
# cookies=driver.get_cookies()
# print("Sizeof cookies",len(cookies))
#
# for c in cookies:
#     print(c)

#delete specific cookie from the browser.
# driver.delete_cookie("mycookie")
# cookies=driver.get_cookies()
# print("Sizeof cookies Afetr deleted one",len(cookies))
#
# for c in cookies:
#     print(c)

#delete All cookies
# driver.delete_all_cookies()
# cookies=driver.get_cookies()
# print("Sizeof cookies Afetr deleted one",len(cookies))
#
# driver.close()