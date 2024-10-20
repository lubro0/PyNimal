import os
import time

os.system('clear')
print("Create folders...")
time.sleep(1)

os.makedirs("config", exist_ok=True)
with open("config/discord_config.txt", "w") as file:
    pass

os.system('clear')
print("\033[92mSuccessful\033[0m")
