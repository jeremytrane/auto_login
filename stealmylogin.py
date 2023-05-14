from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

username = "test"
password = "123"

url = "https://www.stealmylogin.com/demo.html"

# Create a Service object
s = Service("C:\\Users\\Jeremy\\Downloads\\chromedriver_win32\\chromedriver")

# Create a WebDriver instance using the Service object
driver = webdriver.Chrome(service=s)

driver.get(url)

driver.find_element(By.NAME, "username").send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password)
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "input[type=\"submit\" i]").click()
print("Logged in successfully")
time.sleep(7)
driver.close()