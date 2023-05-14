from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

username = "test"
password = "123"

url = "https://accounts.snapchat.com/accounts/v2/login?continue=%2Faccounts%2Fsso%3Fclient_id%3Dweb-calling-corp--prod%26referrer%3Dhttps%253A%252F%252Fweb.snapchat.com%252F%253Fref%253Dsnapchat_dot_com_login_cta"

# Create a Service object to manage the ChromeDriver service
s = Service("C:\\Users\\Jeremy\\Downloads\\chromedriver_win32\\chromedriver")

# Create a WebDriver instance using the Service object and ChromeDriver
driver = webdriver.Chrome(service=s)

# Open the specified URL in the Chrome browser
driver.get(url)
print("Opened page")

# Find the input element with the name "username" and enter the provided username
driver.find_element(By.NAME, "accountIdentifier").send_keys(username)
print("Entered Username")
time.sleep(2)

# Find the submit button element using CSS selector and click on it
driver.find_element(By.CSS_SELECTOR, "button:nth-child(1) span:nth-child(1)").click()
print("Accepted Essential Cookies")

# Wait for the element with CSS selector "#home_children_button" to be clickable
wait = WebDriverWait(driver, 50)
home_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#home_children_button")))

# Click on the element
home_button.click()

# Add any additional steps or actions you need to perform on the page
time.sleep(10)
# Close the browser
driver.quit()
