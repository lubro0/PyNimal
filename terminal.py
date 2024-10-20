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

if os.path.exists("config/discord_config.txt"):
    with open("config/discord_config.txt", "r") as file:
        lines = file.readlines()
    if any("user_id=" in line for line in lines):
        pass
    else:
        user_id = input("What is your Discord user ID? ")
        with open("config/discord_config.txt", "w") as file:
            file.write(f"user_id={user_id}\n")
