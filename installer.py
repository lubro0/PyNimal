import os
import time

os.system('clear')
if os.path.exists("README.md"):
    os.remove("README.md")
print("\033[90mPyNimal v1.0\033[0m")
time.sleep(3)
os.system('clear')
print("Installing PIP packages...")
time.sleep(1)
os.system('pip install asyncio requests')
os.system('clear')
print("\033[92mFinished\033[0m")
time.sleep(1)
os.remove("installer.py")
