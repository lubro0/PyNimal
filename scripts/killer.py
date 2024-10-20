import os
import signal

os.system('clear')
os.kill(os.getpid(), signal.SIGTERM)
