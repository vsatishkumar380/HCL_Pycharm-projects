from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options)
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

#Self
#https://money.rediff.com/gainers/bse/daily/groupa
#SELF://a[contains(text(),'Finolex Industries')]/self::a
# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Vijaya Diagnostic')]/self::a").text
# print(text_msg)

#PARENT
# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Vijaya Diagnostic')]/parent::td").text
# print(text_msg)#parent has no value and navigating to self element, so it will print self element values.


#chaild
# msg=driver.find_elements(By.XPATH,"//a[contains(text(),'Vijaya Diagnostic')]/ancestor::tr/child::td")
# print(len(msg))
#     "or"
# for x in msg:
#     print(x.text)


#ancestor
# msg=driver.find_element(By.XPATH,"//a[contains(text(),'Vijaya Diagnostic')]/ancestor::tr").text
# print(msg) #Vijaya Diagnostic A 679.00 708.50 + 4.34
# driver.close()


#descendant
# msg=driver.find_elements(By.XPATH,"//a[contains(text(),'Vijaya Diagnostic')]/ancestor::tr/descendant::*")
# print(len(msg))
# for x in msg:
#      print(x.text)
# driver.close()

#following
# fllow=driver.find_elements(By.XPATH,"//a[contains(text(),'Vijaya Diagnostic')]/ancestor::tr/following::*")
# print(len(fllow))
# driver.close()

#following-sibling
# fllowsib=driver.find_elements(By.XPATH,"//a[contains(text(),'Vijaya Diagnostic')]/ancestor::tr/following-sibling::*")
# print(len(fllowsib))
# driver.close()

#preceding
#pred=driver.find_elements(By.XPATH,"//a[contains(text(),'Vijaya Diagnostic')]/ancestor::tr/preceding::*")
# pred=driver.find_elements(By.XPATH,"//a[contains(text(),'Vijaya Diagnostic')]/preceding::*")
# print(len(pred))
# driver.close()

#preceding-sibling
# pred=driver.find_elements(By.XPATH,"//a[contains(text(),'Vijaya Diagnostic')]/ancestor::tr/preceding-sibling::*")
# print(len(pred))
# driver.close()




