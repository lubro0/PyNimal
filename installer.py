import os

os.system("clear")
os.system("pkg update && pkg upgrade")
os.system("pkg install wget")
os.system("clear")
print("\033[93mInstalling Version...\033[0m")
os.system("wget https://github.com/lubro0/PyNimal/blob/main/version.txt -O version.txt")
os.system("clear")
with open("version.txt", "r") as f:
    version = f.read().strip()
print(f"\033[92mVersion: {version}\033[0m")
os.system("clear")
