# FIO4 - Pin 10 RPI // Emergency Or Reset
# FIO3 - Pin 11 // Emergency or Reset
# FIO2 - Pin 12 // Enable signal
# FIO1 - Pin 13 // Counter Clockwise Rotation
# FIO0 - Pin 15 // Clockwise Rotation
# VS - Pin 2 // 5V in
# GND - Pin 6 // Ground

import RPi.GPIO as GPIO
import time

def emergency_button(channel):
    print("Emergency Stop")
    GPIO.output(12, False)

def reset_button(channel):
    print("Reset Button")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# enable and rotation initialization
GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12, 100) # enable
GPIO.setup(13, GPIO.OUT) # ctrclockwise rotation
GPIO.setup(15, GPIO.OUT) # clockwise rotation

# start off the Pulse width modulation at 0
pwm.start(0)

# button initialation
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(10, GPIO.RISING, callback=emergency_button)
GPIO.add_event_detect(11, GPIO.RISING, callback=reset_button)

GPIO.output(13, True)
GPIO.output(15, False)

check = 0

while True:
    print("MENU")
    print("1 - Turn On")
    print("2 - Turn Counter Clockwise")
    print("3 - Turn Clockwise")
    print("4 - Change speed 50")
    print("5 - Change speed 25")
    print("6 - Change speed 10")
    print("7 - Change speed 100")
    print("8 - Turn Off")
    print("9 - Exit Program")
    check = int(input("Option ==>"))

    if check == 1:
        print("Turning on...")
        GPIO.output(15, True)
    elif check == 2:
        print("Setting CTR Clockwise...")
        GPIO.output(13, True)
        GPIO.output(15, False)
    elif check == 3:
        print("Setting Clockwise...")
        GPIO.output(13, False)
        GPIO.output(15, True)
    elif check == 4:
        print("50 Speed...")
        pwm.ChangeDutyCycle(50)
    elif check == 5:
        print("25 Speed...")
        pwm.ChangeDutyCycle(75)
    elif check == 6:
        print("10 Speed")
        pwm.ChangeDutyCycle(90)
    elif check == 7:
        print("100 Speed")
        pwm.ChangeDutyCycle(0)
    elif check == 8:
        print("Turning off...")
        GPIO.output(12, False)
    elif check == 9:
        print("Exiting...")
        GPIO.output(12, False)
        GPIO.cleanup()
        exit()
    else:
        print("Incorrect, try again.")
GPIO.cleanup()