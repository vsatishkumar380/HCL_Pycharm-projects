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

#Booking dummy return ticket.
check_box=driver.find_element(By.XPATH,"//li[@class='product-item selected']")
check_box.click()
#print(check_box.text)
price_tag=driver.find_element(By.XPATH,"//li[@class='product-item selected']//span[@class='woocommerce-Price-amount amount']").text
#print(price_tag)

#Passenger details:
driver.find_element(By.XPATH,"//input[@id='travname']").send_keys("Satheesh kumar")
driver.find_element(By.XPATH,"//input[@id='travlastname']").send_keys("Vankadaru")
driver.find_element(By.XPATH,"//textarea[@id='order_comments']").send_keys("Please allocate window seat.")

#selecting the date of birth

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


#selecting the male or female:
gender=driver.find_elements(By.XPATH,"//input[@id='sex_1' or @id='sex_2']")
gender[0].click()

#selecting city:
driver.find_element(By.XPATH,"//input[@id='fromcity']").send_keys("Hyderabad")
driver.find_element(By.XPATH,"//input[@id='tocity']").send_keys("Tiruvuru")

#selecting date:
date="18"

driver.find_element(By.XPATH,"//input[@id='departon']").click()
date_month=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
date_month.select_by_visible_text("Aug")

date_year=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
date_year.select_by_visible_text("2024")

date_obj=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for ele in date_obj:
    if ele.text==date:
        ele.click()
        break




#Selecting Email option

driver.find_element(By.XPATH,"(//input[@id='deliverymethod_1'])[1]").click()


#Billing Details
driver.find_element(By.XPATH,"//input[@id='billname']").send_keys("Satheesh kumar")
driver.find_element(By.XPATH,"(//input[@id='billing_phone'])[1]").send_keys("8096277980")
driver.find_element(By.XPATH,"//input[@id='billing_email']").send_keys("vsatishkumar.380@gmail.com")
driver.find_element(By.XPATH,"(//input[@id='billing_address_1'])[1]").send_keys("Fl203,Ace infra,Kondapur")
driver.find_element(By.XPATH,"//input[@id='billing_postcode']").send_keys("500084")
driver.find_element(By.XPATH,"(//input[@id='billing_city'])[1]").send_keys("Hyderabad")


#boostrap drop down
driver.find_element(By.XPATH,"(//span[@id='select2-billing_state-container'])[1]").click()
states=driver.find_elements(By.XPATH,"(//ul[@id='select2-billing_state-results'])/li")
print(len(states))
states[0].click()


total=driver.find_element(By.XPATH,"//table[@class='shop_table woocommerce-checkout-review-order-table']/tfoot/tr[2]/td").text

if total==price_tag:
    print("Test case verified")
else:
    print("Test case failed.")




