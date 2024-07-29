from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options)


driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()

outer_frame=driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outer_frame) #here webelement passed the input.

#For printing inside the text in MultipleFrames ==>Nested iFrames
# val=driver.find_element(By.XPATH,"/html/body/section/div/div/h5").text
# print(val)


inner_frame=driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")
driver.switch_to.frame(inner_frame) #now we are in inner frame

driver.find_element(By.XPATH,"/html/body/section/div/div/div/input").send_keys("Hello Satish")
print(driver.find_element(By.XPATH,"/html/body/section/div/h5").text)

#Going inner frame to outer frame:
driver.switch_to.parent_frame()
val=driver.find_element(By.XPATH,"/html/body/section/div/div/h5").text
print(val) #output:Nested iFrames

#Going main webpage:
driver.switch_to.default_content()


