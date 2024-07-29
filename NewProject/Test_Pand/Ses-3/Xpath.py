from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
#obsolute ==>
# driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a').click()

#Relative xpath ==> syntax: //tagname[@attribute="value"] or //*[@attribute="value"]
# driver.find_element(By.XPATH,'''//input[@name="q"]''').send_keys('Nokia Lumia 1020')
# driver.find_element(By.XPATH,'//button[@type="submit"]').click()

#operators(and,or,contains(),starts with(), text()) along with XPATH:
# driver.find_element(By.XPATH,"//input[@id='small-searchterms' and @name='q']").send_keys('Nokia Lumia 1020')
# #driver.find_element(By.XPATH,"//input[@id='small-searchterms' or @name='q']").send_keys('Nokia Lumia 1020')
# driver.find_element(By.XPATH,"//button[@type='submit']").click()

#contains()==>Rgister ==<a href="/register?returnUrl=%2F" class="ico-register" style="" xpath="1">Register</a>
//*[contains(@class,'ico-register')]
//*[contains(@xpath,'1')]

#starts with()
//*[starts-with(@class,'ico-reg') ]
//*[starts-with(@xpath,'1')]


#TEXT()
//a[text()='Register']
Element: <a href="//money.rediff.com/companies/finolex-industries/12190003" style=""> Finolex Industries </a>
//a[contains(text(),'Finolex Industries')]


