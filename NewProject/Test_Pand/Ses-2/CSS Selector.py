from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
servi_obj=Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(service=servi_obj,options=options)
driver.get("https://www.facebook.com/")
driver.maximize_window()

# TAG AND ID  ==> syntax: tagname.valueofID
#driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("satish kumar")
#driver.find_element(By.CSS_SELECTOR,"#email").send_keys("satish kumar")

# TAG AND CLASS ==> syntax: tagname.valueofClass
#driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("satish kumar")
#driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("satish kumar")

#TAG ad ATTRIBUTE ==> syntax: tagname[attrubute=value]
#driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("satish kumar")
#driver.find_element(By.CSS_SELECTOR,"[data-testid=royal_email]").send_keys("satish kumar")


#TAG,CLASS ad ATTRIBUTE ==> tagname.valueofClass[attrubute=value]
driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_email]").send_keys("Hello satish")
driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_pass]").send_keys("123satish")