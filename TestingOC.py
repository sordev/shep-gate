from tkinter import *
import RPi.GPIO as GPIO   # Import the GPIO library.
import time               # Import time library

GPIO.setmode(GPIO.BOARD)  
GPIO.setup(32, GPIO.OUT)  # Set GPIO pin 12 to output mode.
pwm = GPIO.PWM(32, 100)   # Initialize PWM on pwmPin 100Hz frequency
GPIO.setup(31, GPIO.OUT) #Direction

app = Tk()
app.title("Test GUI")
app.geometry('475x700')

pwm.start(0)


def OpenGate():
    cState.configure(text="Gate Status: Opens")
    GPIO.output(31, GPIO.HIGH)
    pwm.ChangeDutyCycle(95)
    time.sleep(3)             # wait 3 seconds at current LED brightness
    pwm.ChangeDutyCycle(0)
    
    
     
def CloseGate():
    cState.configure(text="Gate Status: Closed")
    GPIO.output(31, GPIO.LOW)
    pwm.ChangeDutyCycle(95)
    time.sleep(3)             # wait 3 seconds at current LED brightness
    pwm.ChangeDutyCycle(0)
   
name = "Gate #1"
BtA = 500
BtB = 450
AuxSt = "off"

#letu = PhotoImage(file="letulogo.gif")
#l = Label(app, image=letu)
#l.place(x=20,y=5)
#herdx = PhotoImage(file="herdxlogo.gif")
#h=Label(app, image=herdx)
#h.place(x=350, y=5)

cState = Label(app, text = "Gate Status: ", font=("Arial Bold", 15))
cState.place(x=0,y=30)

cName = Label(app, text = "Gate Name: " + name, font=("Arial Bold", 15))
cName.place(x=0,y=5)

gbutton=PhotoImage(file="square.gif")
open = Button(app, image = gbutton, text="Open", command = OpenGate, height = 25, width = 75, compound= RIGHT)
open.place(x=15,y=60)

rbutton=PhotoImage(file="squarered.gif")
open = Button(app, image = rbutton, text="Close", command = CloseGate, height = 25, width = 75, compound= RIGHT)
open.place(x=130,y=60)

cBstat = Label(app, text = "Battery Status", font=("Arial Bold", 15))
cBstat.place(x=0,y=100)

cBatA = Label(app, text = "Battery A: "+ str(BtA) +" w/h", font=("Arial", 11))
cBatA.place(x=0,y=125)

cBatB = Label(app, text = "Battery B: "+ str(BtB) +" w/h", font=("Arial", 11))
cBatB.place(x=0,y=145)

cABstat = Label(app, text = "Aux Batt Status", font=("Arial Bold", 15))
cABstat.place(x=250,y=100)

cABat = Label(app, text = AuxSt, font=("Arial", 11))
cABat.place(x=300,y=125)

app.mainloop()
