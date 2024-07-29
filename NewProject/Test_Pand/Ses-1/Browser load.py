from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
#driver = webdriver.Chrome()
#driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")



