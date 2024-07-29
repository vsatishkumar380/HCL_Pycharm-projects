import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options)
driver.implicitly_wait(10)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

frame_ele=driver.find_element(By.XPATH,"//iframe[@class='demo-frame']")
driver.switch_to.frame(frame_ele)

#method1
#mm/dd/yyyy
# driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("06/02/2024")

#method2

month="September"
year="2025"
date="22"
driver.find_element(By.XPATH,"//input[@id='datepicker']").click()

while True:
    mth=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yer=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    if mth==month and yer==year:
        break
    else:
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click() #forword
        #driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']").click() #backword forword

dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for ele in dates:
    if ele.text==date:
        ele.click()

time.sleep(10)

driver.close()




