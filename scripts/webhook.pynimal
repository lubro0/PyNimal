import requests
import json

def send_discord_webhook():
    with open('config/webhook.txt', 'r') as f:
        webhook_url = f.read().strip()

    embed = {
        "title": "PyNimal Logs",
        "description": "A user has run PyNimal",
        "color": 65280
    }

    data = {
        "embeds": [embed]
    }

    response = requests.post(webhook_url, data=json.dumps(data), headers={"Content-Type": "application/json"})

if __name__ == "__main__":
    send_discord_webhook()
  
