import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options)
driver.implicitly_wait(10)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()


date="17"

driver.find_element(By.XPATH,"//input[@id='dob']").click()
date_month=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
date_month.select_by_visible_text("Sep")

date_year=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
date_year.select_by_visible_text("1991")

date_obj=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for ele in date_obj:
    if ele.text==date:
        ele.click()
        break











