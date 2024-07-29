from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[normalize-space()='nopCommerce']").click()


#getting window id for current window.
winID=driver.current_window_handle
print(winID) #B2B64FC76054831D7387C928E9BDA881
     # 2nd ==>DF7F180E3F6ACEA5B8F91F65786A8157

#getting window id for all open windows.
winIDs=driver.window_handles
print(winIDs)


#Approch1

# parent_wind=winIDs[0]
# Chaild_wind=winIDs[1]
#
# print(parent_wind,Chaild_wind)
#
# driver.switch_to.window(Chaild_wind)
# print(driver.title) #Free and open-source eCommerce platform. ASP.NET Core based shopping cart. - nopCommerce
#
# driver.switch_to.window(parent_wind)
# print(driver.title) #nopCommerce demo store
#
# driver.quit() #all windows will close.
# driver.close() #first window will coles only next windoe present


#Approch2:  more than 2 windows:
# for wind in winIDs:
#     driver.switch_to.window(wind)
#     print(driver.title)
#     if driver.title == "nopCommerce demo store":
#         break  #like that you can stop the right window



#Approch2: close the specific browsers only.
# for wind in winIDs:
#     driver.switch_to.window(wind)
#     print(driver.title)
#     if driver.title == "nopCommerce demo store":
#         driver.close()
#         break






