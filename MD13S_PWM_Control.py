from unittest import case # import case function
import RPi.GPIO as GPIO  # using Rpi.GPIO module
from time import sleep  # import function sleep for delay

GPIO.setmode(GPIO.BCM)  # GPIO numbering
GPIO.setwarnings(False)  # enable warning from GPIO

# PWM | Dir | Out A | Out B   |
# ----+-----+-------+---------+
#   0 |  x  | Low   | Low     |
#   1 |  0  | High  | Low     |
#   1 |  1  | Low   | High    |

# Motor Shield  |   NodeMCU     |   GPIO    |   Purpose
# ---------------+---------------+-----------+-----------
# A-Dir         | Dir (Motor A) |   4       | Direction
# A Speed       | PWMA(Motor A) |   5       | Speed


AN1 = 32  # set pwm1 pin on MD10-hat
DIG1 = 5  # set dir1 pin on MD10-Hat

GPIO.setup(AN1, GPIO.OUT)  # set pin as output
GPIO.setup(DIG1, GPIO.OUT)  # set pin as output
sleep(1)  # delay for 1 seconds
p1 = GPIO.PWM(AN1, 100)  # set pwm for M1

userstring = input("Enter command: Open, Close, or STOP ")

case1: userstring == "Open"
    print("Opening")  # display "Open" when program run
    GPIO.output(DIG1, GPIO.HIGH)  # set DIG1 as HIGH, M1B will turn ON
    p1.start(100)  # set speed for M1 at 100%
    sleep(2)  # delay for 2 second
    break;
case2: userstring == "Close"
    print("Closing")
    GPIO.output(DIG1, GPIO.LOW)
    p1.start(100)
    sleep(2)
    case3: userstring == "STOP"
     break;
print("STOPPING")
    GPIO.output(DIG1, GPIO.LOW)  # Direction can ignore
    p1.start(0)  # set speed for M1 at 0%
    sleep(3)  # delay for 3 second
    break;
