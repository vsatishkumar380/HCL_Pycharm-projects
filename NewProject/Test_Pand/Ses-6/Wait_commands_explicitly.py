from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
servi_obj=Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(service=servi_obj,options=options)
my_wait=WebDriverWait(driver,10,ignored_exceptions=[NoSuchElementExecption,ElementNotVisibleExecption,]) #explicity wait declaration


driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

search_link=my_wait.until(EC.presence_of_element_located(By.XPATH,"//input[@name='q']"))
search_link.send_keys('Nokia Lumia 1020')

#driver.find_element(By.XPATH,'''//input[@name="q"]''').send_keys('Nokia Lumia 1020')
driver.close()