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



#mouse hover Ex:1

# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.maximize_window()
#
#
# #login
# driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
# driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
# driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
#
# #leave->my leave
# leave=driver.find_element(By.XPATH,"//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='Leave']")
# act=ActionChains(driver)
# act.move_to_element(leave).click().perform()
#
# #my leave
# # my_leave=driver.find_element(By.XPATH,"//a[normalize-space()='My Leave']")
# # act.move_to_element(my_leave).click().perform()
#
# #my entities
# entity=driver.find_element(By.XPATH,"//span[normalize-space()='Entitlements']")
# act.move_to_element(entity).click().perform()
#
# drop=driver.find_elements(By.XPATH,"//ul[@role='menu']/li")
# print(len(drop))
# drop[1].click()


#mouse hover Ex:2
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

widget=driver.find_element(By.XPATH,"//a[normalize-space()='Widgets']")
auto_compl=driver.find_element(By.XPATH,"//a[normalize-space()='AutoComplete']")

act=ActionChains(driver)
act.move_to_element(widget).move_to_element(auto_compl).click().perform()
print(driver.title)









