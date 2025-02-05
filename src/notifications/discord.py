import requests
from datetime import datetime
from config.settings import WEBHOOK_URL
from src.utils.logger import log_status, log_success, log_error


def send_startup_notification(total_courses):
    embed = {
        "title": "Elrama is Here",
        "color": 3553599,  # warna ijo
        "description": "I'm not shy. I just have no interest in talking to you, I do a thing called what I want.",
        "fields": [
            {
                "name": "Status",
                "value": "```🟢 Online```",
                "inline": True
            },
            {
                "name": "Total Matkul",
                "value": f"```{total_courses}```",
                "inline": True
            }
            # {
            #     "name": "Timestamp",
            #     "value": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            #     "inline": False
            # }
        ],
        "timestamp": datetime.now().isoformat()
    }

    payload = {
        # "content": "🚀 EL SIRAMA Monitoring Bot is now running!",
        "embeds": [embed]
    }

    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        response.raise_for_status()
        log_success("Discord konek aman lee")
    except Exception as e:
        log_error(f"Failed to send startup notification: {str(e)}")


def send_slot_change_notification(course_data, previous_slot, current_slot, is_selected=False):
    # Previous implementation remains the same
    course_type = "Mata Kuliah Terpilih" if is_selected else "Mata Kuliah"
    log_status(f"Preparing notification for {course_data['subject_name']}...")

    embed = {
        "title": f"Perubahan Slot {course_type}!",
        "color": 65280,
        "fields": [
            {
                "name": "Mata Kuliah",
                "value": f"```💾 {course_data['subject_name']} ({course_data['subject_code']})```",
                "inline": False
            },
            {
                "name": "Kelas",
                "value": f"```🏠 {course_data['class']}```",
                "inline": True
            },
            {
                "name": "Slot Sebelumnya",
                "value": f"```{previous_slot}```",
                "inline": True
            },
            {
                "name": "Slot Sekarang",
                "value": f"```{current_slot}```",
                "inline": True
            }
        ],
        "timestamp": datetime.now().isoformat()
    }

    payload = {
        "content": f"@everyone Slot {course_type.lower()} bertambah!\n{course_data['subject_name']} ({course_data['class']}) bertambah dari {previous_slot} menjadi {current_slot}",
        "embeds": [embed]
    }

    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        response.raise_for_status()
        log_success("Notifikasi berhasil dikirim ke discord")
    except Exception as e:
        log_error(f"Failed to send notification: {str(e)}")
