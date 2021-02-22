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
#p1 = GPIO.PWM(AN1, 100)  # set pwm for M1
while(True):
    print("Closing")
    GPIO.output(DIG1, GPIO.LOW)
    GPIO.PWM(AN1, 50)
