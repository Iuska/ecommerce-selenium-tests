from asyncio import wait_for

from Tools.i18n.pygettext import containsAny
from pycparser.ply.yacc import token
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.keys import Keys


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from selenium.common.exceptions import TimeoutException

import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com/login")
# driver.get("https://automationexercise.com/")


#
wait = WebDriverWait(driver, 10)
time.sleep(3)  # wait for initial page load
login_email = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@data-qa='login-email']")))
login_email.send_keys("sigdelayuh@gmail.com")
time.sleep(2)

login_pass = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Password']")))
login_pass.send_keys("YourStrongPassword123")
time.sleep(2)

login_pass = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']")))
login_pass.click()
time.sleep(2)


#click on navbar of product
products_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/products']")))
products_link.click()


# Wait for the search input and enter the search text
search_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='search_product']")))
search_input.send_keys("H&M")

time.sleep(1)

# Click on the search button/icon
search_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class='fa fa-search']")))
search_button.click()
print("Successfully search")

time.sleep(5)

driver.execute_script("window.scrollBy(0, 300);")
time.sleep(1)

# element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='col-sm-9 padding-right']//div[2]//div[1]//div[1]//div[2]//div[1]//a[1]")))
# element.click()


#view  a product details
product_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='col-sm-9 padding-right']//div[2]//div[1]//div[2]//ul[1]//li[1]//a[1]")))
product_link.click()
print("view product click")

add_to_cart = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add to cart']")))
add_to_cart.click()
print("clcik add button")

view_cart_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//u[normalize-space()='View Cart']/parent::a")))
view_cart_link.click()
print("view chart click")
time.sleep(4)


checkout_details=wait.until(EC.presence_of_element_located((By.XPATH,"//a[normalize-space()='Proceed To Checkout']")))
checkout_details.click()
time.sleep(3)

message_box = wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@name='message']")))
message_box.send_keys("This is my message.")
print("✅ Message typed in textarea.")
time.sleep(2)



place_order=wait.until(EC.presence_of_element_located((By.XPATH,"//a[normalize-space()='Place Order']")))
place_order.click()
time.sleep(2)


card_name = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='name_on_card']")))
card_name.send_keys("Ayushka Sigdel")

card_number = driver.find_element(By.XPATH, "//input[@name='card_number']")
card_number.send_keys("1234 5678 9012 3456")

cvc = driver.find_element(By.XPATH, "//input[@placeholder='ex. 311']")
cvc.send_keys("123")

expiry_mm = driver.find_element(By.XPATH, "//input[@placeholder='MM']")
expiry_mm.send_keys("08")

expiry_yyyy = driver.find_element(By.XPATH, "//input[@placeholder='YYYY']")
expiry_yyyy.send_keys("2030")


button_submit=wait.until(EC.presence_of_element_located((By.XPATH,"//button[@id='submit']")))
button_submit.click()
time.sleep(2)
button_continue=wait.until(EC.presence_of_element_located((By.XPATH,"//a[normalize-space()='Continue']")))
button_continue.click()
print("checkout done")










