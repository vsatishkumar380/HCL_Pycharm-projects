from selenium import webdriver
from selenium.webdriver.chrome.service import Service
servuce_objt=Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(service=servuce_objt,options=options)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")