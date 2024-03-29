# FIO2 - Pin 12 // Enable signal
# FIO1 - Pin 13 // Counter Clockwise Rotation
# GND - Pin 14 // Ground
# FIO0 - Pin 15 // Clockwise Rotation

import RPi.GPIO as GPIO
import time

def emergency_button(channel):
    print("\nEmergency Stop")
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
    print("8 - Turn Motor 90 clkwise for 5 seconds then back")
    print("9 - Turn Motor 90 ctrclkwise for 5 seconds then back")
    print("10 - Turn Off")
    print("11 - Exit Program")
    print("12 - Re Print Menu")

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
        GPIO.output(12, True)
        GPIO.output(13, True)
        GPIO.output(15, False)
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
    elif check == 8:
        pwm.ChangeDutyCycle(80)
        GPIO.output(13, False)
        GPIO.output(15, True)
        time.sleep(0.5)
        GPIO.output(13, True)
        GPIO.output(15, True)
        time.sleep(5)
        GPIO.output(13, True)
        GPIO.output(15, False)
        time.sleep(0.5)
        GPIO.output(13, True)
        GPIO.output(15, True)
    elif check == 9:
        pass
    elif check == 10: # Stop the motor
        GPIO.output(15, True)
        GPIO.output(13, True)
        GPIO.output(12, True)
        print("Turning off...")
    elif check == 11:
        print("Exiting...")
        GPIO.output(12, False)
        GPIO.output(13, True)
        GPIO.output(15, True)
        GPIO.cleanup()
        exit()
    elif check == 12:
        reprintMenu()
    else:
        print("Incorrect, try again.")
GPIO.cleanup()