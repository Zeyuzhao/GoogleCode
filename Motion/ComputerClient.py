import requests
import threading
import time
from datetime import datetime

COMP_ADDRESS = "raspberrypi"

f = open("motionhist.txt", "a")

def logMotion():
    f.write("Motion Occured: " + str(datetime.now()) + "\n")

def run_check():
    r = requests.get("http://" + COMP_ADDRESS + "/motion")
    if (r.json()["motion"]):
        logMotion()
        print("Motion Dectected!")
        return True
    else:
        print("None!")
        return False

if __name__ == "__main__":
    while True:
        m = run_check()
        if m:
            time.sleep(10)
        else:
            time.sleep(2)
