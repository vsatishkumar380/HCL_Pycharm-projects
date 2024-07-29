from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
servi_obj=Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(service=servi_obj,options=options)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
driver.find_element(By.ID,"small-searchterms").send_keys("Nokia Lumia 1020")
driver.find_element(By.XPATH,'''//*[@id="small-search-box-form"]/button''').click()
driver.find_element(By.LINK_TEXT,"Nokia Lumia 1020").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Lumia 1020").click()
driver.close()