#type: ignore
import board
import time
import digitalio
import pwmio

motor = pwmio.PWMOut(board.GP14,duty_cycle = 65535,frequency=5000)

while (True):
    motor.duty_cycle = 4000
    print(board.GP10) #digital
    print(board.GP11) #analog
    print(board.GP12) #I2C
    print(board.GP13) #encoder
