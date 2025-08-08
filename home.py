from Tools.i18n.pygettext import containsAny
from pycparser.ply.yacc import token
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from selenium.common.exceptions import TimeoutException

import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com/")

wait = WebDriverWait(driver, 10)
time.sleep(3)  # wait for initial page load    "//input[@data-qa='login-email']
login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Signup / Login']")))
login_btn.click()
print("Login button is clicked")
time.sleep(2)

#enter the name
name_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Name']")))
name_input.send_keys("Ayuska")
time.sleep(2)
 #enter the email address

email_input=wait.until(EC.presence_of_element_located((By.XPATH,"//input[@data-qa='signup-email']")))
email_input.send_keys("sigdelayuh@gmail.com")
time.sleep(2)

signup=wait.until(EC.presence_of_element_located((By.XPATH,"//button[normalize-space()='Signup']")))
signup.click()
print("sign up sucessfully")
time.sleep(2)


#login
gender = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='id_gender2']")))
gender.click()
time.sleep(3)
# driver.find_element(By.XPATH, "//input[@id='id_gender2']").click()
# name_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='name']")))
# name_input.send_keys("Ayushka")
# time.sleep(2)
password_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password']")))
password_input.send_keys("YourStrongPassword123")
time.sleep(3)


# === Select Day ===
day_dropdown = Select(wait.until(EC.presence_of_element_located((By.ID, "days"))))
day_dropdown.select_by_value("21")  # Selects 21st
time.sleep(2)

# === Select Month ===
month_dropdown = Select(wait.until(EC.presence_of_element_located((By.ID, "months"))))
month_dropdown.select_by_value("12")  # Selects December
time.sleep(2)

# === Select Year ===
year_dropdown = Select(wait.until(EC.presence_of_element_located((By.ID, "years"))))
year_dropdown.select_by_value("1999")  # Selects 1999
time.sleep(2)

#checkbox
newsletter_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='newsletter']")))
newsletter_checkbox.click()

#form
fname = wait.until(EC.presence_of_element_located((By.ID, "first_name")))
fname.send_keys("Ayushkaa")
# time.sleep(1)
lname = wait.until(EC.presence_of_element_located((By.ID, "last_name")))
lname.send_keys("Sigdel")
time.sleep(2)
company=wait.until(EC.presence_of_element_located((By.ID, "company")))
company.send_keys("nnine")
# time.sleep(2)
address=wait.until(EC.presence_of_element_located((By.ID,"address1")))
address.send_keys("maitidevi")
# time.sleep(1)
country_dropdown = Select(wait.until(EC.presence_of_element_located((By.ID, "country"))))
country_dropdown.select_by_visible_text("United States")
print("✅ Country selected: United States")
# time.sleep(1)



state=wait.until(EC.presence_of_element_located((By.ID,"state")))
state.send_keys("pawan marg")
# time.sleep(1)

city=wait.until(EC.presence_of_element_located((By.ID,"city")))
city.send_keys("kathmandu")
# time.sleep(1)


# Fill ZIP Code
zip_code = wait.until(EC.presence_of_element_located((By.ID, "zipcode")))
zip_code.send_keys("9888")
time.sleep(1)

number=wait.until(EC.presence_of_element_located((By.ID,"mobile_number")))
number.send_keys("9877654567")
time.sleep(1)

log=wait.until(EC.presence_of_element_located((By.XPATH,"//button[normalize-space()='Create Account']")))
log.click()
print("➡️ Clicked on Continue, redirected to homepage.")
time.sleep(3)


 
#click on logout button
# logout=wait.until(EC.presence_of_element_located(By.XPATH, "//a[normalize-space()='Logout']")))
# logout.click()
# print("logout sucessfull")

# logout = wait.until(EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Logout']")))
# logout.click()
# print("Logout successful")
