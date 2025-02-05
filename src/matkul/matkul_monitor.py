from src.utils.logger import log_status, log_error
from src.notifications.discord import send_slot_change_notification

class CourseMonitor:
    def __init__(self):
        self.previous_available = {}
        self.previous_selected = {}
    
    def monitor_available_courses(self, available_courses):
        changes = []
        for course in available_courses:
            course_id = course.get('courseid')
            if not course_id:
                continue
                
            current_reservation = course.get('remaining_reservation', 0)
            
            if course_id in self.previous_available:
                previous_reservation = self.previous_available[course_id].get('remaining_reservation', 0)
                if current_reservation > previous_reservation:
                    log_status(f"Available slot changed: {course['subject_name']}: {previous_reservation} -> {current_reservation}")
                    send_slot_change_notification(course, previous_reservation, current_reservation)
                    changes.append((course, previous_reservation, current_reservation))
            
            self.previous_available[course_id] = course.copy()
        return changes

    def monitor_selected_courses(self, selected_courses):
        changes = []
        for course in selected_courses:
            course_id = course.get('courseid')
            if not course_id:
                continue
                
            current_reservation = course.get('remaining_reservation', 0)
            
            if course_id in self.previous_selected:
                previous_reservation = self.previous_selected[course_id].get('remaining_reservation', 0)
                if current_reservation > previous_reservation:
                    log_status(f"Slot matkul dipilih berubah: {course['subject_name']}: {previous_reservation} -> {current_reservation}")
                    send_slot_change_notification(course, previous_reservation, current_reservation, is_selected=True)
                    changes.append((course, previous_reservation, current_reservation))
                elif current_reservation != previous_reservation:
                    log_status(f"Slot matkul reservasi berubah menjadi: {course['subject_name']}: {previous_reservation} -> {current_reservation}")
                    send_slot_change_notification(course, previous_reservation, current_reservation, is_selected=True)
                    changes.append((course, previous_reservation, current_reservation))
            
            self.previous_selected[course_id] = course.copy()
        return changes