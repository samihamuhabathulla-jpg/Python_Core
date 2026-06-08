import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com/")
print(driver.title)
home=driver.find_element(By.XPATH, "//div[@class='item active']//h1")
print("Visible home page:", home.is_displayed())
driver.find_element(By.XPATH, "//a[text()=' Signup / Login']").click()

login_text=driver.find_element(By.XPATH, "//h2[text()='Login to your account']")
print("Login to your account visible:", login_text.is_displayed())

driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys("samihasami205@gmail.com")
driver.find_element(By.XPATH, "//input[@data-qa='login-password']").send_keys("Samiha@2005")

login_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']")))
login_btn.click()
print("Login button click")

logged_in = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Logged in as')]")))
print("Logged In:", logged_in.is_displayed())
print(logged_in.text)

delete_btn=driver.find_element(By.XPATH,"//a[contains(text(),'Delete Account')]")
driver.execute_script("arguments[0].click();", delete_btn)

account_deleted=WebDriverWait(driver, 15).until(EC.visibility_of_element_located( (By.XPATH, "//*[contains(text(),'Account Deleted')]")))
print("ACCOUNT DELETED:", account_deleted.is_displayed())
time.sleep(3)
driver.quit()