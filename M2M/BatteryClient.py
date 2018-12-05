import requests
import threading
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

PIN_NUM = 17
COMP_ADDRESS = "zach-desktop"

GPIO.setup(PIN_NUM, GPIO.OUT)

def setLight(percent):
    if (percent >= 0.2):
        GPIO.output(PIN_NUM, 1)
        print("Turning Light On")
    else:
        GPIO.output(PIN_NUM, 0)
        print("Turning Light Off")
    print(f"Setting Light to {percent}")

def run_check():

    r = requests.get("http://" + "esp8266.local" + "/")
	print(r)
    # bat = r.json()["percent"] / 100
    # setLight(bat)
    # print(f"Battery level: {bat}")

if __name__ == "__main__":
    while True:
        run_check()
        time.sleep(5)
