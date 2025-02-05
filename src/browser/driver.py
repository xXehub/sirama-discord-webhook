import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config.settings import CHROME_OPTIONS
from src.utils.logger import log_status, log_success

def setup_driver():
    log_status("Initializing Chrome WebDriver...")
    chrome_options = webdriver.ChromeOptions()
    for option in CHROME_OPTIONS:
        chrome_options.add_argument(option)

    # pake path chromedriver yang kamu download manual, sesuaikan sama versi chrome mu ya leee
    chromedriver_path = os.path.abspath("chromedriver.exe")  # sesuaikan lokasi filenya disini
    driver = webdriver.Chrome(service=Service(chromedriver_path), options=chrome_options)

    log_success("Webdriver aman leeeeee")
    return driver
