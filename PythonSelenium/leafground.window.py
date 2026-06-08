from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.leafground.com/window.xhtml;jsessionid=node01eod5rah7iwmukgd22nqb57rl17677955.node0")
driver.maximize_window()
parent = driver.current_window_handle
driver.find_element(By.XPATH, "//span[normalize-space()='Open']").click()
time.sleep(5)
all_handles = driver.window_handles
for h in all_handles:
    if h != parent:
        driver.switch_to.window(h)
        driver.close()
driver.switch_to.window(parent)
check = driver.current_window_handle
if parent == check:
    print("Opened and closed the new window")
else:
    print("Opening and closing of new window failed")
driver.quit()