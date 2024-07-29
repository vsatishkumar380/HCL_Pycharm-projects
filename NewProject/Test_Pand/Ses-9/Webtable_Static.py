from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options)
driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#1)count the no of rows and columns
# no_of_rows=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr")
# print("no of rows:",len(no_of_rows)) #7
#
# no_of_columns=driver.find_elements(By.XPATH,"//table[@name='BookTable']//th")
# #//table[@name='BookTable']/tbody/tr[1]/th
# print("no of columns:",len(no_of_columns)) #4
#
# driver.close()

#2)read specific row or column data
# ele1=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[4]/td[3]")
# ele2=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[2]")
# print(ele1.text) #Javascript
# print(ele2.text) #Mukesh
# driver.close()

#3)read all row and column data
# ele=driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr/td")
# print(len(ele))
# for x in ele:
#     print(x.text, end="   ")

#or

# no_of_rows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
# no_of_columns=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//th"))
# print(no_of_rows,no_of_columns)
#
# print("...........printing all rows and columns dataa......")
#
# for r in range(2,no_of_rows+1):
#     for c in range(1,no_of_columns+1):
#         data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#         print(data,end="    ")
#
#     print()


#4)read the data based on condition (list the books whoos aouther is mukesh)

no_of_rows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
no_of_columns=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//th"))
print(no_of_rows,no_of_columns)

print("...........read the data based on condition......")

for r in range(2,no_of_rows+1):
    aurthur_name=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if aurthur_name == "Mukesh":
        Book_name=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text
        Book_price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]").text
        print(Book_name,"====",aurthur_name,"and price is:",Book_price)

driver.close()



