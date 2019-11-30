# FIO4 - Pin 10 RPI // Emergency Or Reset
# FIO3 - Pin 11 // Emergency or Reset
# FIO2 - Pin 12 // Enable signal
# FIO1 - Pin 13 // Counter Clockwise Rotation
# FIO0 - Pin 15 // Clockwise Rotation

from RPi.GPIO import GPIO
import time

def emergency_button(channel):
    print("Emergency Stop")

def reset_button(channel):
    print("Reset Button")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# enable and rotation initialization
pwm = GPIO.PWM(12, 100) # enable
GPIO.setup(13, GPIO.OUT) # ctrclockwise rotation
GPIO.setup(15, GPIO.OUT) # clockwise rotation

# start off the Pulse width modulation at 0
pwm.start(0)

# button initialation
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUB_DOWN)

GPIO.add_event_detect(10, GPIO.RISING, callback=emergency_button)
GPIO.add_event_detect(11, GPIO.RISING, callback=reset_button)

GPIO.output(13, True)
GPIO.output(15, False)

pwm.ChangeDutyCycle(50)

GPIO.output(12, True)

time.sleep(2)

GPIO.output(12, False)