from src.browser.driver import setup_driver
from src.auth.login import login_sirama
from src.matkul.monitor import get_course_data
from src.core.monitor_session import MonitorSession
from src.utils.logger import log_status, log_error, print_banner, log_success
from src.utils.sihub import get_banner
from src.notifications.discord import send_startup_notification

def main():
    # Print ASCII banner sihub wkwk
    print_banner(get_banner())
    
    log_status("Start Elrama Monitoring...")
    driver = setup_driver()
    
    try:
        if not login_sirama(driver):
            log_error("Login failed. Exiting...")
            return
        
        # mengambil initial matkul data
        available_courses, selected_courses = get_course_data(driver)
        total_available = len(available_courses)
        
        # mengirim startup notif embed ke discord webhook
        send_startup_notification(total_available)
            
        # memulai session monitoring
        monitor_session = MonitorSession(driver)
        monitor_session.start(get_course_data)
                
    finally:
        log_status("Shutting down...")
        driver.quit()

if __name__ == "__main__":
    main()