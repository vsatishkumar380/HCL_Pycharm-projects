import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import os
location=os.getcwd()
def Chrome_setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\\Users\\svankada\\Drivers\\chromedriver.exe")
    # download the file at desired location
    #for pdf onther pref added that is:"plugins.always_open_pdf_externally":True
    preferences={"download.default_directory":location,"plugins.always_open_pdf_externally":True}
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    # download the file at desired location
    options.add_experimental_option("prefs", preferences)
    options.add_argument("--disable-adds")
    driver = webdriver.Chrome(service=serv_obj, options=options)
    return driver

def Edge_setup():
    from selenium.webdriver.edge.service import Service
    serv_obj = Service("C:\\Users\\svankada\\Drivers\\msedgedriver.exe")
    # download the file at desired location
    preferences={"download.default_directory":location,"plugins.always_open_pdf_externally":True}
    options = webdriver.EdgeOptions()
    options.add_experimental_option("detach", True)
    # download the file at desired location
    options.add_experimental_option("prefs", preferences)
    options.add_argument("--disable-adds")
    driver = webdriver.Edge(service=serv_obj, options=options)
    return driver

def Firefox_setup():
    from selenium.webdriver.firefox.service import Service
    serv_obj = Service("C:\\Users\\svankada\\Drivers\\geckodriver.exe")
    #setting
    ops=webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk","application/pdf")
    #mine type file:https://www.sitepoint.com/mime-types-complete-list/ --> get req value-> here mine type for pdf is "application/pdf"
    ops.set_preference("browser.download.manager.showWhenStarting", False) #save pop window will not appear
    ops.set_preference("browser.download.manager.folderList", 2) #0-desktop,1-default location,2-desired location
    ops.set_preference("browser.download.dir", location)
    #pdf download
    ops.set_preference("pdf.disabled", True)
    driver = webdriver.Firefox(service=serv_obj,options=ops)
    return driver

#driver=Chrome_setup() #pdf file download is file-sample_150kB
driver=Edge_setup() #pdf file download is file-sample_150kB (1)
# driver=Firefox_setup()
driver.implicitly_wait(10)
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/")
driver.maximize_window()
driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]").click() #file downloaded in C:\Users\svankada\PycharmProjects\NewProject\Test_Pand\Ses-12


