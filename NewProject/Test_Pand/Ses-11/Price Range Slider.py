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

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

min_slider=driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[2]/span[1]")
max_slider=driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[2]/span[2]")

print("....location of sliders before moving....")
print("min_slider location",min_slider.location) #{'x': 59, 'y': 250}
print("max_slider location",max_slider.location) #{'x': 510, 'y': 250}


act=ActionChains(driver)
act.drag_and_drop_by_offset(min_slider,100,0).perform()
act.drag_and_drop_by_offset(max_slider,-40,0).perform()


print("....location of sliders after moving....")
print("min_slider location",min_slider.location) #{'x': 158, 'y': 250}
print("max_slider location",max_slider.location) #{'x': 469, 'y': 250}

driver.close()