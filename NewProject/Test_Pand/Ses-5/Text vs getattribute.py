from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
servi_obj=Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(service=servi_obj,options=options)

driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()

# email_box=driver.find_element(By.XPATH,"//input[@id='Email']")
# time.sleep(3)
# email_box.clear()
# time.sleep(3)
# email_box.send_keys("sathesh@gmail.com")
# print("result of text:",email_box.text) #inner text will capture, if not available returns none.
# print("result of get_attribute:",email_box.get_attribute("value")) #Get value of any attribute of webelent.
# print(email_box.get_attribute("type"))
# print(email_box.get_attribute("id"))
# time.sleep(3)
# driver.close()
#
#
# or

# button=driver.find_element(By.XPATH,"//button[normalize-space()='Log in']")
# print(button.text)
# print(button.get_attribute("value"))
# print(button.get_attribute("type"))
# print(button.get_attribute("class"))