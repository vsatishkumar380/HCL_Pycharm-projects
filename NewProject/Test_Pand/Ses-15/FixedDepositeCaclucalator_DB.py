import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
from selenium.webdriver.support.select import Select
#import mysql.connector ==> add mysql-connector-python libarary.


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

database data
con=mysql.connector.connect(host="localhost",port=3306,user="root",passwd="root",database="mydb")
curs=con.cursor()
curs.execute("select * from caldata") ==>caldata is table from data base, it should be any name in DB.




for row in curs:
    #collect the data from excel
    pricipal = row[0]
    intreast = row[1]
    per1 = row[2]
    per2 = row[3]
    freq = row[4]
    exp_mval = row[5]

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

    #validation
    if float(exp_mval) == float(act_mval):
        print("Test case passed")

    else:
        print("Test case failed")

    #clearing
    driver.find_element(By.XPATH, "//div[@class='CTR PT15']/a[2]").click()

driver.close()

#make sure excel is closed.









































