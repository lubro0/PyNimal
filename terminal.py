import os
import time
import requests

time.sleep(1)
os.system('clear')
print("\033[90mPyNimal v1.0\033[0m")

with open("webhook.env", "r") as file:
    webhook_url = file.read().strip()

data = {
    "embeds": [
        {
            "title": "PyNimal Logs",
            "description": "A user ran PyNimal",
            "color": 65280
        }
    ]
}

requests.post(webhook_url, json=data)
