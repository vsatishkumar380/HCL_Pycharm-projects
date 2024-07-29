from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options)

#def:webpage contains form of other webpage and embaded in this webpage is called frame.
#frame/Iframe
#frame:window applications
#Iframe:web applications

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

#sig_frame=driver.find_element(By.XPATH,"//iframe[@id='singleframe']")
#driver.switch_to.frame(sig_frame) #webelement is input.
#or
driver.switch_to.frame("singleframe") #id is input.
val=driver.find_element(By.XPATH,"/html/body/section/div/h5").text
print(val)
driver.find_element(By.XPATH,"/html/body/section/div/div/div/input").send_keys("Satish")