import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class Browser:
    browser, service = None, None

    # Initialise the webdriver with the path to chromedriver.exe
    def __init__(self, driver: str):
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service=self.service)

    def open_page(self, url: str):
        self.browser.get(url)

    def close_browser(self):
        self.browser.close()


if __name__ == '__main__':
    
    driver_path = "C:\\Users\\Jeremy\Downloads\\chromedriver_win32"
    browser = Browser('driver_path')

    browser.open_page('https://youtube.com/')
    time.sleep(1)

    browser.close_browser()