from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
servi_obj=Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(service=servi_obj,options=options)
driver.get("https://practice.automationtesting.in/")
driver.maximize_window()


#CLASS_NAME==> total will idently no of slides comes under same class.
size=driver.find_elements(By.CLASS_NAME,"n2-ss-slide")
print(len(size))


#TAG_NAME
No_links=size=driver.find_elements(By.TAG_NAME,"a")
print(len(No_links))

driver.close()