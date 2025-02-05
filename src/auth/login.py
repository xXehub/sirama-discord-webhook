from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from config.settings import SIRAMA_LOGIN_URL, USERNAME, PASSWORD
from src.utils.logger import log_status, log_success, log_error
import time


def login_sirama(driver):
    try:
        log_status(f"Mencoba login SIRAMA dengan username: {USERNAME}")

        # ngambil sirama login url
        driver.get(SIRAMA_LOGIN_URL)
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        username_field.clear()
        username_field.send_keys(USERNAME)
        log_status("Username diinputkan")
        
        password_field = driver.find_element(By.NAME, "password")
        password_field.clear()
        password_field.send_keys(PASSWORD)
        log_status("Password diinputkan")
        login_button = driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()

        # interval pergantian url
        WebDriverWait(driver, 10).until(
            EC.url_changes(SIRAMA_LOGIN_URL)
        )

        time.sleep(3)

        # ngecek login page
        if SIRAMA_LOGIN_URL in driver.current_url:
            log_error("Still on login page after attempt")
            try:
                error_msg = driver.find_element(
                    By.CSS_SELECTOR, ".error-message, .alert, .notification").text
                log_error(f"Login error message: {error_msg}")
            except:
                pass
            return False

        log_success("Login berhasil!")
        return True

    except Exception as e:
        log_error(f"Error pas login: {str(e)}")
        return False
