import os
import sys

os.system('clear')

with open("config/version.txt", "r") as file:
    version = file.read().strip()

print(f"\033[90mPyNimal v{version}\033[0m")
print("\n1> Create File")
print("\nexit> Exit PyNimal")
print("reset> Reset PyNimal")

while True:
    choice = input(">>> ")

    if choice == "1":
        filename = input("File Name >>> ")
        os.system(f"nano {filename}")

    if choice.lower() == "exit":
        os.system("pkill -f terminal.py")
        sys.exit()

    if choice.lower() == "reset":
        os.system("rm -rf scripts && rm -rf config && rm -rf terminal.py && git clone --depth 1 --single-branch https://github.com/lubro0/PyNimal.git temp_dir && mv temp_dir/* . && rm -rf temp_dir && python installer.py")
