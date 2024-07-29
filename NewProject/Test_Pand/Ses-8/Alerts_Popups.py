from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options)
import time
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

#clik on alert window
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(5)

alert_window=driver.switch_to.alert

print(alert_window.text)
alert_window.send_keys("Satheesh")
time.sleep(5)
#alert_window.accept() #close the alert window by ok button.
# alert_window.dismiss() #close the alert window by cancel button


# Example 2:
# driver.get("https://mypage.rediff.com/")
# driver.maximize_window()
#
# driver.find_element(By.XPATH,"//input[@value=' Go ']").click()
# alert_win=driver.switch_to.alert
# print(alert_win.text)
# alert_win.accept()
# driver.close()






