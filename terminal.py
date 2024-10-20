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
