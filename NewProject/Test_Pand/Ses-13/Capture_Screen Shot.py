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
driver.maximize_window()

#driver.save_screenshot("C:\\Users\\svankada\\PycharmProjects\\NewProject\\Test_Pand\\Ses-13\\screen_shot_home.png")
driver.save_screenshot(os.getcwd()+"\\screen_shot_home.png")
#driver.get_screenshot_as_file(os.getcwd()+"\\screen_shot_home.png")
# driver.get_screenshot_as_png(os.getcwd()+"\\screen_shot_home.png")
# driver.get_screenshot_as_base64(os.getcwd()+"\\screen_shot_home.png") #save the file in binary format.

driver.close()