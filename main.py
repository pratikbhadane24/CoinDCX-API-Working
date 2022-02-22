import time
import pandas as pd

key = ""  # Your API Key
secret = ""  # Your Secret Key
timeStamp = int(round(time.time() * 1000))

api_end_point = "https://api.coindcx.com/"


# Limits for OHLCV Data
timeframe = "1d"
limit = "100"


class CoinDCX():
    pass


user = CoinDCX()

