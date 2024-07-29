from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
servi_obj=Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(service=servi_obj,options=options)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
print(driver.title) #OrangeHRM
print(driver.current_url) #https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
print(driver.page_source)
driver.close()

# Application commands:
# driver.get() ==> opening the application url
# driver.title ==> to capture the title of cureent web page
# driver.current_url ==> to capture the current url of web page
# driver.page_source ==> to capture sorce code of the web page