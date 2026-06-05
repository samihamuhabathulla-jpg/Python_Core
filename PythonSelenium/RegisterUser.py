from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://automationexercise.com")

wait = WebDriverWait(driver,15)

driver.find_element(By.XPATH,"//a[normalize-space()='Signup / Login']").click()

wait.until(EC.visibility_of_element_located((By.NAME,"name"))).send_keys("Samiha")

driver.find_element(By.XPATH,"//input[@data-qa='signup-email']").send_keys("samiha1245@gmail.com")

signupButton = driver.find_element(By.XPATH,"//button[@data-qa='signup-button']")
driver.execute_script("arguments[0].click();",signupButton)

heading = wait.until(EC.visibility_of_element_located((By.XPATH,"//b[text()='Enter Account Information']")))

print("Heading Text :",heading.text)

if heading.text == "ENTER ACCOUNT INFORMATION":
    print("Verification Successful")
else:
    print("Verification Failed")

driver.find_element(By.ID,"id_gender2").click()

driver.find_element(By.ID,"password").send_keys("Samiha@2005")

driver.find_element(By.XPATH,"//select[@id='days']").click()
driver.find_element(By.XPATH,"//option[@value='16']").click()

driver.find_element(By.XPATH,"//select[@id='months']").click()
driver.find_element(By.XPATH,"//option[@value='3']").click()

driver.find_element(By.XPATH,"//select[@id='years']").click()
driver.find_element(By.XPATH,"//option[@value='2004']").click()

driver.find_element(By.ID,"newsletter").click()
optin = driver.find_element(By.ID,"optin")
driver.execute_script("arguments[0].click();", optin)

driver.find_element(By.ID,"first_name").send_keys("Samiha")
driver.find_element(By.ID,"last_name").send_keys("Muhabathulla")
driver.find_element(By.ID,"company").send_keys("Smartcliff")
driver.find_element(By.ID,"address1").send_keys("RS Puram")
driver.find_element(By.ID,"state").send_keys("Tamil Nadu")
driver.find_element(By.ID,"city").send_keys("Coimbatore")
driver.find_element(By.ID,"zipcode").send_keys("636008")
driver.find_element(By.ID,"mobile_number").send_keys("9876543210")

createAccount = driver.find_element(By.XPATH,"//button[text()='Create Account']")
driver.execute_script("arguments[0].click();",createAccount)

accountCreated = wait.until(EC.visibility_of_element_located((By.XPATH,"//b[text()='Account Created!']")))

print("Message :",accountCreated.text)

if accountCreated.text == "ACCOUNT CREATED!":
    print("Account Created Successfully")
else:
    print("Account Creation Failed")

wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@data-qa='continue-button']"))).click()

deleteButton = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@href='/delete_account']")))
driver.execute_script("arguments[0].click();", deleteButton)

accountDeleted = wait.until(EC.visibility_of_element_located((By.XPATH,"//b[text()='Account Deleted!']")))

print("Message :",accountDeleted.text)

if accountDeleted.text == "ACCOUNT DELETED!":
    print("Account Deleted Successfully")
else:
    print("Account Deletion Failed")

driver.quit()