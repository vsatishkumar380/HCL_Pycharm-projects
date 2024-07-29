import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options)
driver.implicitly_wait(10)



#mouse hover Ex:1

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()


#login
driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()

#PIM
leave=driver.find_element(By.XPATH,"//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='PIM']")
act=ActionChains(driver)
act.move_to_element(leave).click().perform()

add_emp=driver.find_element(By.XPATH,"//a[normalize-space()='Add Employee']")
act.move_to_element(add_emp).click().perform()

driver.find_element(By.XPATH,"//img[@class='employee-image']").click()

keyboard=Controller()
keyboard.type("C:\\Users\\svankada\\Pictures\\cancel.PNG")
keyboard.press(Key.enter)
keyboard.release(Key.enter)