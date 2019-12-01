import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if GPIO.input(10) == True:
        print("Emergency Stop")
    elif GPIO.input(11) == True:
        print("Reset")
    else:
        waiting = input("Waiting...")