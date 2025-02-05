import requests
import json
from config.settings import (
    SIRAMA_API_BASE,
    MATKUL_TERSEDIA,
    MATKUL_DIPILIH,
    ID_FAKULTAS
)
from src.utils.logger import log_status, log_error, log_course_data


def get_course_data(driver):
    try:
        log_status("Fetching matkul data...")

        token = driver.execute_script('return localStorage.getItem("token")')
        if not token:
            log_error("Token ga ketemu")
            return None, None

        token_json = json.loads(token)

        session = requests.Session()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json',
            'Referer': 'https://sirama.telkomuniversity.ac.id/registration/courses',
            'Origin': 'https://sirama.telkomuniversity.ac.id',
            'Authorization': f'Bearer {token_json["token"]}'
        }

        # ngambil data matkul tersedia
        available_courses_by_page = []
        available_courses = []

        for i in range(1, 5):
            url = f"{SIRAMA_API_BASE}/{MATKUL_TERSEDIA}/{ID_FAKULTAS}/{i}"
            response = session.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            available_courses.extend(data)
            available_courses_by_page.append(data)

        # ngambil data matkul yang dipilih
        log_status("Fetching matkul terpilih...")
        selected_url = f"{SIRAMA_API_BASE}/{MATKUL_DIPILIH}/"
        response = session.get(selected_url, headers=headers)
        response.raise_for_status()
        selected_courses = response.json()

        log_course_data(available_courses_by_page, len(selected_courses))
        return available_courses, selected_courses

    except Exception as e:
        log_error(f"Error fetching data matkul: {str(e)}")
        if hasattr(e, 'response'):
            log_error(f"Response content: {e.response.text}")
        return None, None
