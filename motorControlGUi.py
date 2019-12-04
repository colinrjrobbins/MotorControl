import RPi.GPIO as GPIO
from tkinter import *
import tkinter.messagebox

# CLASS: Motor_GUI
# Description: To run a constant motor GUI class that will generate a physical
#              window and allow for easy control over the motor and its functions.
class MotorInterface():
# ---------------- MAIN GUI INITALIZATION ------------------------
    # Function: Initilization
    # Description: Create the main working window. Add the full Tkinter functionality
    def __init__(self, master):
        # Global Class variables used to identify motor on/off and speed values.
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)    

        # enable and rotation initialization
        GPIO.setup(12, GPIO.OUT) # enable input pin
        self.pwm = GPIO.PWM(12, 100) # pulse width modulation

        # rotation initialization
        GPIO.setup(13, GPIO.OUT) # ctr clockwise rotation
        GPIO.setup(15, GPIO.OUT) # clockwise rotation

        # start off the Pulse width modulation at 100
        self.pwm.start(100) # start off with the speed at 0

        # button initialation
        GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        self.motorValue = 1
        self.speedValue = 0
        
        # Interface (tkinter)
        # Motor Direction Label
        # ROW 0, COLUMN 0
        self.lblMotor = Label(master, text="Motor Control", width = 15)
        self.lblMotor.grid(row = 0, column = 0)
        
        # Extra space to split up labels
        # ROW 0, COLUMN 2
        self.lblSpace = Label(master, text="", width = 10)
        self.lblSpace.grid(row = 0, column = 2)
        
        # Label Speed
        # ROW 0, COLUMN 3
        self.lblSpeed = Label(master, text="Speed", width = 10)
        self.lblSpeed.grid(row = 0, column = 3)

        # Start button
        # ROW 1, COLUMN 0
        self.btnStart = Button(master, text="Start", width=10, command = self.StartMotor)
        self.btnStart.grid(row = 1, column = 0)
        
        # Stop button
        # ROW 1, COLUMN 1
        self.btnStop = Button(master, text="Stop", width=10, command = self.StopMotor)
        self.btnStop.grid(row = 1, column = 1)
        
        # Speed Scale
        # ROW 1, COLUMN 3
        self.sclSpeedCtrl = Scale(master, 
                                  from_=20,
                                  to=100,
                                  orient=HORIZONTAL,
                                  length=100,
                                  width=10,
                                  sliderlength=20,
                                  command = self.ControlSpeed)     
        self.sclSpeedCtrl.grid(row = 1, column = 3)

        # Rotation Label
        # ROW 2, COLUMN 0
        self.lblRotation = Label(master, text="Rotation", width = 10)
        self.lblRotation.grid(row = 2,column = 0)
        
        # Rotate Right Button
        # ROW 3, COLUMN 1
        self.btnClockwise = Button(master, text="Clockwise", width = 15, command = self.ClockwiseRotation)
        self.btnClockwise.grid(row = 3, column = 1)

        # Rotate Left Button
        # ROW 3, COLUMN 0
        self.btnCtrClockwise = Button(master, text="Ctr Clockwise", width = 15, command = self.CtrClockwiseRotation)
        self.btnCtrClockwise.grid(row = 3, column = 0)

        # Spacer Row to make stuff look good.
        self.lblSpace2 = Label(master, text="",width = 40)
        self.lblSpace2.grid(row = 4, column = 1)

        # Output Data Label
        # ROW 5, COLUMN 1
        self.lblOutput = Label(master, text="Output Information", width = 40)
        self.lblOutput.config(text='Waiting for user to press Start...')
        self.lblOutput.grid(row = 5, column = 1)

        # Intitialize the slider control as disabled.
        self.sclSpeedCtrl.config(state = DISABLED)
        self.btnClockwise.config(state = DISABLED)
        self.btnCtrClockwise.config(state = DISABLED)
        self.btnStop.config(state = DISABLED)
        
    # END INITIALIZATION FUNCTION

    def StartMotor(self):
        print("Turning on...")
        GPIO.output(15, True)
        GPIO.output(13, False)
        GPIO.output(12, True)
        self.pwm.ChangeDutyCycle(50)
        self.lblOutput["text"] = "Turning on Motor..."

        self.sclSpeedCtrl.config(state = NORMAL)
        self.btnClockwise.config(state = NORMAL)
        self.btnCtrClockwise.config(state = NORMAL)
        self.btnStop.config(state = NORMAL)

    def StopMotor(self):
        print("Turning off...")
        GPIO.output(12, False)
        GPIO.output(13, True)
        GPIO.output(15, True)
        self.lblOutput["text"] = "Turning off Motor..."

        self.sclSpeedCtrl.config(state = DISABLED)
        self.btnClockwise.config(state = DISABLED)
        self.btnCtrClockwise.config(state = DISABLED)

    def ClockwiseRotation(self):
        print("Setting Clockwise...")
        GPIO.output(13, False)
        GPIO.output(15, True)
        self.lblOutput["text"] = "Clockwise Rotation Enable..."

    def CtrClockwiseRotation(self):
        print("Setting CTR Clockwise...")
        GPIO.output(13, True)
        GPIO.output(15, False)
        self.lblOutput["text"] = "Counter Clockwise Rotation Enable..."

    def ControlSpeed(self, value):
        speedValue = 100 - int(value)
        print(str(speedValue))
        self.pwm.ChangeDutyCycle(speedValue)

    def EmergencyButton(self):
        GPIO.output(12, False)
        GPIO.output(13, True)
        GPIO.output(15, True)
        self.btnStart.config(state = DISABLED)

    def ResetButton(self):
        self.btnStart.config(state = NORMAL)

tk_master = Tk()                              
mainGUI = MotorInterface(tk_master)

# Run the program in a main loop until quit
tk_master.mainloop()                  