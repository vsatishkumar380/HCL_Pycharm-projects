from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
servi_obj=Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(service=servi_obj,options=options)
driver.implicitly_wait(10) #seconds, implicity wait, will never wait 10 sec, if element availble in 2 sec and after move.

driver.get("https://www.google.co.in/")
driver.maximize_window()

Search_box=driver.find_element(By.NAME,"q")
Search_box.send_keys("Selenium")
Search_box.submit()

#time.sleep(5) #performance of script will reduced.if used 5 times in it will take 25 sec, some times for loading it willtake
#more than 5 sec, then you get execption error. both wasys dis advantage.

driver.find_element(By.XPATH,"//a[@href='https://www.selenium.dev/']//h3[@class='LC20lb MBeuO DKV0Md'][normalize-space()='Selenium']").click()

driver.close() #here implicity will stop.