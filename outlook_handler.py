import requests
from http.cookies import SimpleCookie

class OutlookHandler:
    def __init__(self, cookies):
        self.session = requests.Session()
        self.cookies = self.load_cookies(cookies)
        self.session.cookies.update(self.cookies)

    def load_cookies(self, cookie_string):
        cookie = SimpleCookie()
        cookie.load(cookie_string)
        return {key: morsel.value for key, morsel in cookie.items()}

    def read_inbox(self):
        url = 'https://outlook.office.com/api/v2.0/me/messages'
        response = self.session.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def extract_otp_codes(self, messages):
        otp_codes = []
        for message in messages:
            if 'OTP' in message['Subject']:
                # Assuming OTP is contained in the body of the email
                otp = self.parse_otp(message['Body']['Content'])
                otp_codes.append(otp)
        return otp_codes

    def parse_otp(self, email_body):
        # Logic to extract OTP from the email body
        # This is a placeholder implementation
        import re
        otp_pattern = r'\d{6}'  # Assuming OTPs are 6 digits
        match = re.search(otp_pattern, email_body)
        return match.group(0) if match else None