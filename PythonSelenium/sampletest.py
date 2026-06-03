from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window()
print(driver.title)
#driver.save_screenshot("Sample.png")
#print(driver.page_source)
time.sleep(5)
driver.quit()   
