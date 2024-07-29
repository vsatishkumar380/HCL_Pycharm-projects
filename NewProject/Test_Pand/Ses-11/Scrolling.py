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

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

#scroll down the page by pixel number
# driver.execute_script("window.scrollBy(0,500)","")
# value=driver.execute_script("return window.pageYOffset;")
# print("Pixel at prest is :",value)



#scroll down the page till element is visible
# ele=driver.find_element(By.XPATH,"//a[@href='demo/on-dom-element.html']") #Context Menu on DOM Element
# driver.execute_script("arguments[0].scrollIntoView();",ele)
# value=driver.execute_script("return window.pageYOffset;")
# print("Pixel at prest is :",value) #878

#scroll down the page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("Pixel at prest is :",value)

time.sleep(5)
#scroll up to starting page:
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("Pixel at prest is :",value)

