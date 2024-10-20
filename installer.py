import os
import time

os.system('clear')
if os.path.exists("README.md"):
    os.remove("README.md")
os.system('pip install asyncio requests')
os.remove("installer.py")
os.system("python terminal.py")
