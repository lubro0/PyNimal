import os
import time
import requests

time.sleep(1)
os.system('clear')
print("\033[90mPyNimal v1.0\033[0m")

data = {
    "embeds": [
        {
            "title": "PyNimal Logs",
            "description": "A user ran PyNimal",
            "color": 65280
        }
    ]
}

requests.post("https://discord.com/api/webhooks/1297565535550177351/QNlGYeWZ2i_lAALeJIMkk7Xty9Tx1EVlQI3ouQCdXRhXpxaBfN469xdvq4M_k9y2dMvI", json=data)
