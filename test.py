from tkinter import *
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26,GPIO.OUT)

app = Tk()
app.title("Test GUI")
app.geometry('650x650')



def OpenGate():
    cState.configure(text="Gate Status: Open")
    GPIO.output(26,GPIO.HIGH)
     
def CloseGate():
    cState.configure(text="Gate Status: Closed")
    GPIO.output(26,GPIO.LOW)
   

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
