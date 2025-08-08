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


# ✅ Scroll slowly after login
scroll_pause_time = 0.3  # seconds between each scroll
scroll_step = 100        # pixels per scroll
max_scrolls = 10         # only scroll a few times

# Get total scrollable height
scroll_height = driver.execute_script("return document.body.scrollHeight")

# # Perform incremental scroll
# for i in range(0, scroll_height, scroll_step):
#     driver.execute_script(f"window.scrollTo(0, {i});")
#     time.sleep(scroll_pause_time)
#
# # Optional: wait at bottom
# time.sleep(2)
#
#
# women_Section=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[normalize-space()='Women']")))
# women_Section.click()
# time.sleep(2)


for i in range(0, scroll_height, scroll_step):
    driver.execute_script(f"window.scrollTo(0, {i});")
    time.sleep(scroll_pause_time)

    # try:
    #     women_section = driver.find_element(By.XPATH, "//a[normalize-space()='Women']")
    #     if women_section.is_displayed() and women_section.is_enabled():
    #         women_section.click()
    #         time.sleep(3)
    #         print("✅ 'Women' section clicked.")
    #         break

    try:
        # kid_section = driver.find_element(By.XPATH, "//a[normalize-space()='Kids']")
        # if kid_section.is_displayed() and kid_section.is_enabled():
        #     kid_section.click()
        #     time.sleep(3)
        #     print("✅ 'kid' section clicked.")
        #     break
        madbrand_section = driver.find_element(By.XPATH, "//a[@href='/brand_products/Madame']")
        if madbrand_section.is_displayed() and madbrand_section.is_enabled():
            madbrand_section.click()
            time.sleep(3)
            print("✅ 'Madame' section clicked.")

        break

    except (NoSuchElementException, ElementClickInterceptedException):
        continue  # element not found or not clickable yet

# === Scroll again to find and click "View Product" ===
for _ in range(max_scrolls):
    driver.execute_script(f"window.scrollBy(0, {scroll_step});")
    time.sleep(3)

    try:
        view_product = driver.find_element(By.XPATH, "//div[5]//div[1]//div[2]//ul[1]//li[1]//a[1]")
        if view_product.is_displayed() and view_product.is_enabled():
            view_product.click()
            print("✅ 'View Product' clicked.")
            time.sleep(2)
            break
    except (NoSuchElementException, ElementClickInterceptedException):
        continue

quantity_product=driver.find_element(By.XPATH,"//input[@id='quantity']")
quantity_product.click()
time.sleep(3)
# Press UP arrow key 3 times to increase by 3
for _ in range(2):
    quantity_product.send_keys(Keys.ARROW_UP)
    time.sleep(2)

#for review
review_name=driver.find_element(By.XPATH,"//input[@id='name']")
review_name.send_keys("Ayushka")
print("name is clicked")
time.sleep(3)

review_email=driver.find_element(By.XPATH,"//input[@id='email']")
review_email.send_keys("ayus@gmail.com")
print("email is clicked")
time.sleep(3)

review_message=wait.until(EC.presence_of_element_located((By.ID,"review")))
review_message.send_keys("I want to buy this product")
print("message is typed")
time.sleep(2)

# 🔽 Scroll down a little to bring the Submit button into view
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(1)

submit=wait.until(EC.presence_of_element_located((By.ID,"button-review")))
submit.click()
time.sleep(3)

# ✅ Scroll to top after submit
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(5)
print("✅ Scrolled to top after submitting review.")

#add to cart button
add_to_cart=wait.until(EC.presence_of_element_located((By.XPATH,"//button[normalize-space()='Add to cart']")))
add_to_cart.click()
time.sleep(5)

# continue_alert=wait.until(EC.presence_of_element_located((By.XPATH,"/div[@class='modal-footer']")))
# continue_alert.click()
# time.sleep(5)

cart_details=wait.until(EC.presence_of_element_located((By.XPATH,"//u[normalize-space()='View Cart']")))
cart_details.click()
time.sleep(6)

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

