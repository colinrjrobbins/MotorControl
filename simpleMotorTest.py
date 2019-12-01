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
    GPIO.output(13, True)
    GPIO.output(15, True)

def reset_button(channel):
    print("Reset Button")
    
def reprintMenu():
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
    print("10 - Re Print Menu")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# enable and rotation initialization
GPIO.setup(12, GPIO.OUT) # enable input pin
pwm = GPIO.PWM(12, 100) # pulse width modulation

# rotation initialization
GPIO.setup(13, GPIO.OUT) # ctr clockwise rotation
GPIO.setup(15, GPIO.OUT) # clockwise rotation

# start off the Pulse width modulation at 100
pwm.start(100) # start off with the speed at 0

# button initialation
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# button event detections for reset and for emergency button
GPIO.add_event_detect(10, GPIO.RISING, callback=emergency_button)
GPIO.add_event_detect(11, GPIO.RISING, callback=reset_button)

# initialize for counter clockwise start
GPIO.output(13, True)
GPIO.output(15, False)

# initialize the check as 0
check = 0

# have infinite loop to display menu
reprintMenu()
while True:
    check = int(input("Option ==>"))

    if check == 1: # initialize the motor and start clockwise
        print("Turning on...")
        GPIO.output(15, True)
        GPIO.output(13, False)
        GPIO.output(12, True)
        pwm.ChangeDutyCycle(50)
    elif check == 2: # counterclockwise
        print("Setting CTR Clockwise...")
        GPIO.output(13, True)
        GPIO.output(15, False)
    elif check == 3: # clockwise
        print("Setting Clockwise...")
        GPIO.output(13, False)
        GPIO.output(15, True)
    elif check == 4: # half speed
        print("50% Speed...")
        pwm.ChangeDutyCycle(50)
    elif check == 5: # 25% speed
        print("25% Speed...")
        pwm.ChangeDutyCycle(75)
    elif check == 6: # 10% speed
        print("10% Speed")
        pwm.ChangeDutyCycle(90)
    elif check == 7: # 100% spped
        print("100% Speed")
        pwm.ChangeDutyCycle(0)
    elif check == 8: # Stop the motor
        print("Turning off...")
        GPIO.output(12, False)
        GPIO.output(13, True)
        GPIO.output(15, True)
    elif check == 9:
        print("Exiting...")
        GPIO.output(12, False)
        GPIO.output(13, True)
        GPIO.output(15, True)
        GPIO.cleanup()
        exit()
    elif check == 10:
        reprintMenu()
    else:
        print("Incorrect, try again.")
GPIO.cleanup()