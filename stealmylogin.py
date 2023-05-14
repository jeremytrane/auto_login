from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

username = "test"
password = "123"

url = "https://www.stealmylogin.com/demo.html"

# Create a Service object to manage the ChromeDriver service
s = Service("C:\\Users\\Jeremy\\Downloads\\chromedriver_win32\\chromedriver")

# Create a WebDriver instance using the Service object and ChromeDriver
driver = webdriver.Chrome(service=s)

# Open the specified URL in the Chrome browser
driver.get(url)

# Find the input element with the name "username" and enter the provided username
driver.find_element(By.NAME, "username").send_keys(username)

# Find the input element with the name "password" and enter the provided password
driver.find_element(By.NAME, "password").send_keys(password)

# Pause the execution for 2 seconds to allow time for the page to load
time.sleep(2)

# Find the submit button element using CSS selector and click on it
driver.find_element(By.CSS_SELECTOR, "input[type=\"submit\" i]").click()

# Print a message indicating that the login was successful
print("Logged in successfully")

# Pause the execution for 7 seconds to allow time for further actions or observations
time.sleep(7)

# Close the browser and terminate the WebDriver session
driver.close()
