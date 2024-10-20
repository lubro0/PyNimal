import os
import time

os.system('clear')

with open("config/version.txt", "r") as file:
    version = file.read().strip()

print(f"\033[90mPyNimal v{version}\033[0m")
print("\n1> Create File")

while True:
    choice = input(">>> ")

    if choice == "1":
        print("\033[91mSoon\033[0m")
        time.sleep(1)
    else:
        print("\033[91mInvalid\033[0m")
