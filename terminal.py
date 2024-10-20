import os

os.system('clear')

with open("config/version.txt", "r") as file:
    version = file.read().strip()

print(f"\033[90mPyNimal v{version}\033[0m")
print("\n1> Create File")
print("reset> Reset PyNimal")
print("exit> Exit PyNimal")

while True:
    choice = input(">>> ")

    if choice == "1":
        print("\033[91mSOON\033[0m")
    elif choice.lower() == "exit":
        break
