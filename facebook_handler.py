import requests
import json

class FacebookAPI:
    def __init__(self, app_id, app_secret):
        self.app_id = app_id
        self.app_secret = app_secret
        self.access_token = None

    def register(self, username, password):
        # Simulated registration process
        data = {'username': username, 'password': password}
        response = requests.post('https://graph.facebook.com/v10.0/registration', json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'Registration failed: {response.text}')

    def send_otp(self, phone):
        # Simulated OTP sending process
        data = {'phone': phone}
        response = requests.post('https://graph.facebook.com/v10.0/send_otp', json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'Failed to send OTP: {response.text}')

    def verify_otp(self, phone, otp):
        # Simulated OTP verification process
        data = {'phone': phone, 'otp': otp}
        response = requests.post('https://graph.facebook.com/v10.0/verify_otp', json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'OTP verification failed: {response.text}')

    def create_account(self, username, password, phone):
        try:
            self.register(username, password)
            self.send_otp(phone)
            otp = input('Enter the OTP sent to your phone: ')
            self.verify_otp(phone, otp)
            print('Account created successfully!')
        except Exception as e:
            print(f'An error occurred: {e}')