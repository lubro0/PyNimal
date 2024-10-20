import os
import time

os.system('clear')
if os.path.exists("README.md"):
    os.remove("README.md")
print("\033[90mPyNimal v1.0\033[0m")
time.sleep(1)
os.system('clear')
print("We uninstall Rust because it causes problems")
time.sleep(2)
os.system('pkg update && pkg upgrade && pkg uninstall rust')
