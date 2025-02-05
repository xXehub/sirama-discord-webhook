import requests
from src.utils.logger import log_status, log_success
from config.settings import SIRAMA_LOGIN_URL, SIRAMA_BASE_URL, USERNAME, PASSWORD
import json

def setup_client():
    log_status("Setting up HTTP client...")
    
    try:
        session = requests.Session()
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Origin': 'https://sirama.telkomuniversity.ac.id',
            'Referer': 'https://sirama.telkomuniversity.ac.id/auth/login',
        })
        response = session.get(SIRAMA_LOGIN_URL)
        response.raise_for_status()
        login_data = {
            "username": USERNAME,
            "password": PASSWORD,
            "submit": "true"
        }
        login_url = f"{SIRAMA_BASE_URL}/api/auth/login" 
        response = session.post(
            login_url,
            json=login_data,
            headers={
                'Content-Type': 'application/json'
            }
        )
        
        if response.ok and 'token' in response.text:
            token_data = response.json()
            session.headers.update({
                'Authorization': f'Bearer {token_data["token"]}'
            })
            session.token = token_data
            log_success("Client setup successful")
            return session
        else:
            raise Exception(f"Login failed: {response.text}")
            
    except Exception as e:
        log_status(f"Failed to setup client: {str(e)}")
        raise