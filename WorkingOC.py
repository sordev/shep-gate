from tkinter import *
#import BG_MT
#import os
import RPi.GPIO as GPIO   # Import the GPIO library.
import time               # Import time library

GPIO.setmode(GPIO.BOARD)  
GPIO.setup(32, GPIO.OUT)  # Set GPIO pin 12 to output mode.
pwm = GPIO.PWM(32, 100)   # Initialize PWM on pwmPin 100Hz frequency
GPIO.setup(31, GPIO.OUT) #Direction

app = Tk()
app.title("Test GUI")
app.geometry('650x650')

pwm.start(0)


def OpenGate():
    cState.configure(text="Gate Status: Open")
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
   

letu = PhotoImage(file="letulogo.gif")
l = Label(app, image=letu)
l.place(x=20,y=5)
herdx = PhotoImage(file="herdxlogo.gif")
h=Label(app, image=herdx)
h.place(x=350, y=5)

cState = Label(app, text = "Gate Status: ", font=("Arial Bold", 25))
cState.place(x=0,y=150)

gbutton=PhotoImage(file="square.gif")
open = Button(app, image = gbutton, text="Open", command = OpenGate, height = 50, width = 150, compound= RIGHT)
open.place(x=50,y=300)

rbutton=PhotoImage(file="squarered.gif")
open = Button(app, image = rbutton, text="Close", command = CloseGate, height = 50, width = 150, compound= RIGHT)
open.place(x=250,y=300)


app.mainloop()
