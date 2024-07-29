from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options)
driver.implicitly_wait(10)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()


#login
driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()


#amin-->usermangement-->users
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click()
driver.find_element(By.XPATH,"//li[@class='oxd-topbar-body-nav-tab --parent --visited']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Users']").click()

no_rows=len(driver.find_elements(By.XPATH,"//div[@class='oxd-table-body']/div"))
print("Total no of row in tablw:",no_rows)

for r in range(1,no_rows+1):
    status=driver.find_element(By.XPATH,"//div[@class='oxd-table-body']/div["+str(r)+"]/div/div[5]").text
    if status=="Disabled":
        user_name=driver.find_element(By.XPATH,"//div[@class='oxd-table-body']/div["+str(r)+"]/div/div[2]").text
        print("username is Disabled of name is:",user_name)
    else:
        print("N0 user name is  Disabled:", user_name)





