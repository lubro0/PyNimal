import os
import time

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

user_id = input("What is your Discord user ID? ")
with open("config/discord_config.txt", "w") as file:
    file.write(f"user_id={user_id}\n")
