from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests as requests
serv_obj=Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options)
import time
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

total_links=driver.find_elements(By.TAG_NAME,"a")
print("Total links",len(total_links))
count=0
for link in total_links:
    url=link.get_attribute("href")
    try:
        resp=requests.head(url)
    except:
        None
    if resp.status_code >= 400:
        print("It is a broken link:",url)
        count=count+1
    else:
        print("It is not a broken link:", url)

print("Total broken links",count)

