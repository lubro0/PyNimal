import os
import time

with open("version.txt", "r") as file:
    version = file.read().strip()

print(f"PyNimal v{version}")
time.sleep(2)
os.remove(version.txt)
