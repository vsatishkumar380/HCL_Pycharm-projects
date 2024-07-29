from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
servi_obj=Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(service=servi_obj,options=options)

driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()

# is_displayed()
# is_enabled()

# dis_play=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
# print("Display status:",dis_play.is_displayed()) #True
# print("Enabled status:",dis_play.is_enabled()) #True
# driver.close()


# is_selected() ==> for radio buttons and check box
rd_male=driver.find_element(By.XPATH,"//input[@id='gender-male']")
rd_female=driver.find_element(By.XPATH,"//input[@id='gender-female']")
print("Male status:",rd_male.is_selected()) #if not selected gives false boolen value ==>False
print("Female status:",rd_female.is_selected()) #False
rd_male.click()
print("After selecting Male status:",rd_male.is_selected())
print("Female status:",rd_female.is_selected())
driver.close()