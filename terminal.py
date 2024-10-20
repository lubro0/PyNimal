import os
import time

with open("version.txt", "r") as file:
    version = file.read().strip()

print(f"PyNimal v{version}")
time.sleep(2)

os.remove("version.txt")

os.makedirs("Scripts", exist_ok=True)

with open("Scripts/help.txt", "w") as help_file:
    help_file.write("""Made by lubro__
https://github.com/lubro0

Thanks for using PyNimal!
There is currently no help""")
