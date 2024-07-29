import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
from selenium.webdriver.support.select import Select
import XLUtill as Excel


serv_obj=Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
options.add_argument("--disable-notifications")
driver=webdriver.Chrome(service=serv_obj,options=options)
driver.implicitly_wait(10)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/hsbc/fixed-deposit-calculator-ZZZ-BHS001.html?classic=true")
driver.maximize_window()

#allow the popup button.
#driver.find_element(By.XPATH,"//*[@id='wzrk-confirm']").click() #if "disable-notifications" is not added, this one req.

#Excel data
file="C:\\Users\\svankada\\Work\\Satish\\Personal\\Python\\V Satheesh Kumar\\Selenium-Python\\Scren shots\\SES-14 Data driven testing using excel\\Simple_intrest_data.xlsx"
rows=Excel.getRowCount(file,"Sheet1")
print(rows)


#collect the data from excel
pricipal = Excel.readData(file,"Sheet1",2,1)
intreast = Excel.readData(file, "Sheet1", 2, 2)
per1 = Excel.readData(file, "Sheet1", 2, 3)
per2 = Excel.readData(file, "Sheet1", 2, 4)
freq = Excel.readData(file, "Sheet1", 2, 5)
exp_mval = Excel.readData(file, "Sheet1", 2, 6)

    #web peform
driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(pricipal)
driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(intreast)
driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(per1)
period = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
period.select_by_visible_text(per2)

frequence = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
frequence.select_by_visible_text(freq)
driver.find_element(By.XPATH, "//div[@class='CTR PT15']/a[1]").click()
act_mval=driver.find_element(By.XPATH,"//span[@id='resp_matval']/strong").text
print(act_mval)