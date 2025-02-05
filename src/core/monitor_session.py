import time
from datetime import datetime
from src.utils.logger import log_status, log_error, log_success, log_waiting
from src.matkul.matkul_monitor import CourseMonitor

class MonitorSession:
    def __init__(self, driver):
        self.driver = driver
        self.course_monitor = CourseMonitor()
        self.check_count = 0
        
    def start(self, get_course_data):
        # log_success("Bot aktif dan menginfo matkul")
        
        while True:
            try:
                self.check_count += 1
                current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                log_status(f"Check #{self.check_count} at {current_time}")
                
                available_courses, selected_courses = get_course_data(self.driver)
                
                if not available_courses or not selected_courses:
                    log_error("Failed to get course data")
                    self._wait_and_continue()
                    continue
                
                # Monitor courses
                self.course_monitor.monitor_available_courses(available_courses)
                self.course_monitor.monitor_selected_courses(selected_courses)
                
                self._wait_and_continue()
                
            except Exception as e:
                log_error(f"Error in main loop: {str(e)}")
                self._wait_and_continue()
    
    def _wait_and_continue(self, seconds=60):
        log_waiting(seconds)
        time.sleep(seconds)