from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import requests as requests
serv_obj=Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options)
import time
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()
#time.sleep(15)
# dropdown_ele=driver.find_element(By.XPATH,"//select[@name='DateOfBirthMonth']")
# drp_country=Select(dropdown_ele)

#select the option from dropdown.
# drp_country.select_by_visible_text("January")  #select by name showed on webpage
# drp_country.select_by_index(9) #select by index order ==> september
# drp_country.select_by_value("5") #select by value="6" ==> June
# time.sleep(5)
# driver.close()

#capture the all options and print them.
# Total_opt=drp_country.options
# print(len(Total_opt))
#
# for month in Total_opt:
#     print(month.text)

#select the option from dropdown without buit-in functions:
# Total_opt=drp_country.options
#
# for opt in Total_opt:
#     if opt.text == "January":
#         opt.click()
#         break


#Useing "option" not using select class.
total_opt=driver.find_elements(By.XPATH,"//*[@name='DateOfBirthMonth']/option")
print(len(total_opt))
for opt in total_opt:
    print(opt.text)

driver.close()

