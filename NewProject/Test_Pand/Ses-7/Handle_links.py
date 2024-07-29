import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options)
import time
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# 1)internal and external links.
#clink on link
#driver.find_element(By.XPATH,"(//a[normalize-space()='Digital downloads'])[1]").click()

#find no of links on a webpage
#links=driver.find_elements(By.XPATH,"//a")
#or
# links=driver.find_elements(By.TAG_NAME,"a")
# print("Total no of links:",len(links)) #96
# for i in links:
#     print(i.text)
# driver.close()


#2) broken links: