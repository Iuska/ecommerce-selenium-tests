from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
driver = webdriver.Chrome()
driver.maximize_window()


driver.get("https://automationexercise.com/contact_us")

wait = WebDriverWait(driver, 10)
time.sleep(3)  #

name=wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Name']")))
name.send_keys("Ayushka")
time.sleep(2)

email = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Email']")))
email.send_keys("sigdel@gmail.com")
time.sleep(2)

subject = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Subject']")))
subject.send_keys("QA test")
time.sleep(2)

message = wait.until(EC.element_to_be_clickable((By.XPATH, "//textarea[@id='message']")))
message.send_keys("This is a test message")
time.sleep(2)

#choose file
upload_file = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@name='upload_file']")))
upload_file.send_keys(r"C:\Users\Acer\Desktop\pre.pdf")
time.sleep(4)