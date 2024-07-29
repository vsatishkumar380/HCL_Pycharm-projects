from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service_obj=Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(service=service_obj,options=options)
driver.get("https://www.google.com")
driver.maximize_window()




