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

driver.find_element(By.XPATH,"//a[normalize-space()='YouTube']").click()
time.sleep(5)
#driver.close() #==> sigle parent browser will close
#driver.quit()#Will close all windows in browser

