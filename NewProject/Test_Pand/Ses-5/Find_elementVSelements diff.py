from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
servi_obj=Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(service=servi_obj,options=options)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#######  find_element () -->returns single webelement

#1) locator matching with single web elemet
# element=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
# element.sens_keys("Nokia Lumia 1020")

#2) locator matching with multiple web elemets
# element=driver.find_element(By.XPATH,"//div[@class='footer-upper']//a")
# print(element.text) #return 1 webelement
# driver.close()

#3) element not available then throw nosuchelement exeception.
# login_element=driver.find_element(By.LINK_TEXT,"Login") #exceptions.NoSuchElementException:
# login_element.click()
# time.sleep(5)
# driver.close()


#######  find_element () -->returns multiple webelements

#1) locator matching with single web elemet
# element=driver.find_elements(By.XPATH,"//input[@id='small-searchterms']") #elemets always return list.
#
# print(len(element)) # will return 1 webelemet becuase, webelement is locating one element not elements
# # for x in element:
# #      print(x.send_keys("Nokia Lumia 1020"))
# # time.sleep(5)
# # driver.close()
# #   OR
# element[0].send_keys("Nokia Lumia 1020")
# driver.close()


#2) locator matching with multiple web elemets
# element=driver.find_elements(By.XPATH,"//div[@class='footer-upper']//a")
# print(len(element)) #return 1 webelement
# #print(element[0].text) #Sitemap
# # OR
# for x in element:
#     print(x.text)
# driver.close()

#3) element not available
# login_element=driver.find_elements(By.LINK_TEXT,"Login") #no exceptions error.
# print(len(login_element)) #if not mattching the elemet/elemts return emty list and no exception error
# driver.close()








