import hmac
import hashlib
import json
import time
import requests
import pandas as pd

key = ""  # Your API Key
secret = ""  # Your Secret Key
timeStamp = int(round(time.time() * 1000))

api_end_point = "https://api.coindcx.com/"


# Limits for OHLCV Data
timeframe = "1d"
limit = "100"


class CoinDCX():

    def login(self, endpoint):
        secret_bytes = bytes(secret, encoding='utf-8')
        json_body = json.dumps(self.body, separators=(',', ':'))
        signature = hmac.new(secret_bytes, json_body.encode(),
                             hashlib.sha256).hexdigest()
        url = f"{api_end_point}{endpoint}"

        self.headers = {
            'Content-Type': 'application/json',
            'X-AUTH-APIKEY': key,
            'X-AUTH-SIGNATURE': signature
        }
        response = requests.post(
            url, data=json_body, headers=self.headers)
        data = response.json()
        return data

    def user_details(self):
        self.body = {"timestamp": timeStamp}
        endpoint = "exchange/v1/users/info"
        data = self.login(endpoint)
        print(
            f"Logged in as: {data['first_name']} {data['last_name']}\nUserID: {data['coindcx_id']}")
        self.fname = data['first_name']
        self.lname = data['last_name']


user = CoinDCX()
user.user_details()
