import os
import time
import requests

os.system('clear')
print("Create folders...")
time.sleep(1)

if not os.path.exists("config"):
    os.makedirs("config")
    with open("config/discord_config.txt", "w") as file:
        pass

print("\033[92mSuccessful\033[0m")
time.sleep(1)
os.system('clear')

input("Please join this Discord Server: https://discord.gg/EsdZSbAe2B\n")
os.system('clear')

user_id = None
if os.path.exists("config/discord_config.txt"):
    with open("config/discord_config.txt", "r") as file:
        lines = file.readlines()
    if any("user_id=" in line for line in lines):
        user_id = next(line.split("=")[1].strip() for line in lines if "user_id=" in line)
    else:
        user_id = input("What is your Discord user ID? ")
        with open("config/discord_config.txt", "w") as file:
            file.write(f"user_id={user_id}\n")

if user_id:
    webhook_url = "https://discord.com/api/webhooks/1297573788497739827/7UzLQclcjKAWAA5J54wJlASxpLVbbOq7CQ6RP-V5FYMAOcK64VjO57LXAzoaLXz5rw6H"
    
    requests.post(webhook_url, json={"content": f"<@{user_id}>"})
    
    embed_data = {
        "embeds": [
            {
                "title": "Logs",
                "description": "You have entered PyNimal successfully",
                "color": 65280
            }
        ]
    }
    
    requests.post(webhook_url, json=embed_data)
