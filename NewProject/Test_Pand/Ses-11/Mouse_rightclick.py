import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options)
driver.implicitly_wait(10)



#mouse right click Ex:1

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

button=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")

act=ActionChains(driver)


for i in range(28):
    act.context_click(button).perform()
    time.sleep(10)
    driver.find_element(By.XPATH,"//span[normalize-space()='Copy']").click()
    time.sleep(15)
    driver.switch_to.alert.accept()
    time.sleep(10)
    print("Hi")
    time.sleep(5)
#driver.close()