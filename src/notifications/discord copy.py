import requests
from datetime import datetime
from config.settings import WEBHOOK_URL
from src.utils.logger import Logger

class DiscordNotifier:
    def __init__(self):
        self.logger = Logger()
        self.webhook_url = WEBHOOK_URL

    def send_startup_notification(self):
        embed = {
            "title": "🤖 Elrama Matkul Monitor",
            "description": "Bot telah aktif dan mulai memantau perubahan slot mata kuliah",
            "color": 3447003,  # Blue color
            "fields": [
                {
                    "name": "Status",
                    "value": "✅ Online",
                    "inline": True
                },
                {
                    "name": "Start Time",
                    "value": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    "inline": True
                }
            ],
            "footer": {
                "text": "Elrama"
            },
            "timestamp": datetime.now().isoformat()
        }

        payload = {
            "content": "🚀 Bot Monitor Elrama telah aktif!",
            "embeds": [embed]
        }

        try:
            response = requests.post(self.webhook_url, json=payload)
            response.raise_for_status()
            self.logger.log_success("Discord startup aman")
        except Exception as e:
            self.logger.log_error(f"Failed to send startup notification: {str(e)}")

    def send_slot_change_notification(self, course_data, previous_slot, current_slot, is_selected=False):
        course_type = "Mata Kuliah Terpilih" if is_selected else "Mata Kuliah"
        self.logger.log_status(f"Preparing notification for {course_data['subject_name']}...")
        
        embed = {
            "title": f"📊 Perubahan Slot {course_type}!",
            "color": 65280,
            "fields": [
                {
                    "name": "Mata Kuliah",
                    "value": f"{course_data['subject_name']} ({course_data['subject_code']})",
                    "inline": False
                },
                {
                    "name": "Kelas",
                    "value": course_data['class'],
                    "inline": True
                },
                {
                    "name": "Slot Sebelumnya",
                    "value": str(previous_slot),
                    "inline": True
                },
                {
                    "name": "Slot Sekarang",
                    "value": str(current_slot),
                    "inline": True
                }
            ],
            "footer": {
                "text": "SIHUB Course Monitor"
            },
            "timestamp": datetime.now().isoformat()
        }
        
        payload = {
            "content": f"@everyone Slot {course_type.lower()} bertambah!\n{course_data['subject_name']} ({course_data['class']}) bertambah dari {previous_slot} menjadi {current_slot}",
            "embeds": [embed]
        }
        
        try:
            response = requests.post(self.webhook_url, json=payload)
            response.raise_for_status()
            self.logger.log_success("Notification sent successfully")
        except Exception as e:
            self.logger.log_error(f"Failed to send notification: {str(e)}")