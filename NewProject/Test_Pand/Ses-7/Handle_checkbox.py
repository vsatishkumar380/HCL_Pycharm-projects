from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options)

# driver.get("https://artoftesting.com/samplesiteforselenium")
# driver.maximize_window()


#1)Select specific check box
#driver.find_element(By.XPATH,"//input[@value='Automation']").click()

#2)Select two check boxs:
# Two_check=driver.find_elements(By.XPATH,"//input[@value='Automation' or @value='Performance']")
# for x in Two_check:
#     x.click()


#3)Select multiple check boxs: for monday to saturday
#mul_check=driver.find_elements(By.XPATH,"//input[@type='checkbox' or contains(@id,'day')]")
# print(len(mul_check)) #7
#aproch1
# for i in range(len(mul_check)):
#     mul_check[i].click()

#aproch2
# for x in mul_check:
#     x.click()

#aproch3 my choice
# for i in mul_check:
#     name=i.get_attribute('id')
#     if name == "firday" or name == "sunday":
#         i.click()


driver.get("https://www.ironspider.ca/forms/checkradio.htm")
driver.maximize_window()

color=driver.find_elements(By.XPATH,"//input[@name='color' and contains(@value,'e')]")

#1)choice of selecton:
# for i in color:
#     find=i.get_attribute('value')
#     if find == "yellow" or find == "green":
#         i.click()


# 2)clear all check boxes
# for i in color:
#     i.click()
#
# for x in color:
#     if x.is_selected():
#         x.click()


