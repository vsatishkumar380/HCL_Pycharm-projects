import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options)
driver.implicitly_wait(10)

driver.get("https://text-compare.com/")
driver.maximize_window()

#steps to be perform:
# 1)write a text through send key.
# 2)select the text ==> Cntrl+A
# 3)Copy the text ==>Cntrl+C
# 4)Move to next slide==> tab
# 5)Paste the text ==>Cntrl+v

# 1)write a text through send key.
input1=driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
input1.send_keys("Hi Satheesh How are you")

act=ActionChains(driver)

# 2)select the text ==> Cntrl+A
# act.key_down(Keys.CONTROL)
# act.send_keys("a")
# act.key_up(Keys.CONTROL)
# act.perform()
time.sleep(3)
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()


# 3)Copy the text ==>Cntrl+C
# act.key_down(Keys.CONTROL)
# act.send_keys("c")
# act.key_up(Keys.CONTROL)
# act.perform()
time.sleep(3)
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

# 4)Move to next slide==> tab
# act.send_keys(Keys.TAB)
# act.perform()
act.send_keys(Keys.TAB).perform()

# 5)Paste the text ==>Cntrl+v
# act.key_down(Keys.CONTROL)
# act.send_keys("v")
# act.key_up(Keys.CONTROL)
# act.perform()
act.key_down(Keys.CONTROL).send_keys("").key_up(Keys.CONTROL).perform()


#Click on New tap:
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

reg_per=Keys.CONTROL+Keys.RETURN
driver.find_element(By.LINK_TEXT,"Register").send_keys(reg_per)









