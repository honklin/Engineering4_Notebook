#type: ignore
import board
import time
from adafruit_motor import motor
import pwmio
import digitalio
import analogio

pwmA = pwmio.PWMOut(board.GP14, frequency=50)
pwmB = pwmio.PWMOut(board.GP15, frequency=50)
motor1 = motor.DCMotor(pwmA,pwmB)

ch1 = analogio.AnalogIn(board.GP26)
ch2 = analogio.AnalogIn(board.GP27)

while True:
    motor1.throttle = .2
    print("ch1:")
    print(ch1.value)
    print("ch2:")
    print(ch2.value)
    time.sleep(.1)