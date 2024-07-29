from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options)
import time
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#search by word and find the links and open the all links and close specific links.

driver.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("python")
driver.find_element(By.XPATH,"//input[@type='submit']").click()

time.sleep(5)
res=driver.find_elements(By.XPATH,"//*[contains(text(),'Python')]")
print(len(res))

for ele in res:
    ele.click()

winIDs=driver.window_handles
print(winIDs)

lst=[]
for wind in winIDs:
    driver.switch_to.window(wind)
    nam=driver.title
    lst.append(nam)
    if nam == "Python (missile) - Wikipedia" or nam == "Python - Wikipedia":
        driver.close()

print(lst)















