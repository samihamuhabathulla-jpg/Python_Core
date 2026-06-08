import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

# Open Website
driver.get("https://automationexercise.com/")

print(driver.title)

# Verify Home Page
home = driver.find_element(By.XPATH, "//div[@class='item active']//h1")
print("Visible home page:", home.is_displayed())

# Click Signup / Login
signup_login = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(text(),'Signup / Login')]")
    )
)

driver.execute_script("arguments[0].click();", signup_login)

# Wait for Login Page
login_text = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located(
        (By.XPATH, "//h2[text()='Login to your account']")
    )
)

print("Login page loaded successfully")
# Enter Email and Password
driver.find_element(
    By.XPATH,
    "//input[@data-qa='login-email']"
).send_keys("samihaaa@gmail.com")

driver.find_element(
    By.XPATH,
    "//input[@data-qa='login-password']"
).send_keys("Sami@05")

# Click Login
login_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[text()='Login']")
    )
)
driver.execute_script("arguments[0].click();", login_btn)
print("Login button clicked")

# Verify Logged In
logged_in = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Logged in as')]")))
driver.execute_script("arguments[0].click();", login_btn)
print("Login button clicked")

# Click Delete Account
delete_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(text(),'Delete Account')]")
    )
)
delete_btn.click()

# Verify Account Deleted
account_deleted = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located(
        (By.XPATH, "//b[text()='Account Deleted!']")
    )
)

print("Account Deleted:", account_deleted.is_displayed())

time.sleep(3)
driver.quit()