from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from pynput.keyboard import Key, Controller
serv_obj=Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options)
import time
driver.get("https://login.microsoftonline.com/189de737-c93a-4f5a-8b68-6f4ca9941912/wsfed?wa=wsignin1.0&wtrealm=https%3a%2f%2fm.myhcl.com%2fWFH%2fDefault.aspx&wctx=rm%3d0%26id%3dpassive%26ru%3d%252fWFH%252fDigitalAct.aspx&wct=2024-06-17T07%3a19%3a50Z&wreply=https%3a%2f%2fm.myhcl.com%2fWFH%2fDefault.aspx&sso_reload=true&sso_nonce=AwABEgEAAAACAOz_BQD0_73-5fjvmKZ7GKvXyWQ7v89MZ7aR1c2ea461ZCHdOf02m1hwWUHaUuINOn-EOZyRm0Kpyu-L-SRVNUuzxVITSsQgAA&client-request-id=36919f55-c656-498e-9830-e58daa42c747&mscrid=36919f55-c656-498e-9830-e58daa42c747")
driver.maximize_window()
driver.implicitly_wait(10)


keyboard=Controller()
keyboard.press(Key.tab)
keyboard.release(Key.tab)

time.sleep(2)

keyboard.press(Key.tab)
keyboard.release(Key.tab)

# time.sleep(2)

keyboard.press(Key.tab)
keyboard.release(Key.tab)

# time.sleep(2)

keyboard.press(Key.tab)
keyboard.release(Key.tab)

# time.sleep(2)

keyboard.press(Key.tab)
keyboard.release(Key.tab)

# time.sleep(2)

keyboard.press(Key.tab)
keyboard.release(Key.tab)



keyboard.press(Key.enter)
keyboard.release(Key.enter)


time.sleep(2)
keyboard.type("vankadarusath.v@hcltech.com")
time.sleep(2)
keyboard.press(Key.enter)
keyboard.release(Key.enter)


time.sleep(3)
keyboard.type("Joshvik@2020")
time.sleep(2)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(15)
keyboard.press(Key.enter)
keyboard.release(Key.enter)