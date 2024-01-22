#type: ignore
import board
<<<<<<< HEAD:raspberry-pi/test.py
import time
import digitalio
import pwmio
=======
import pwmio
import digitalio
import analogio
>>>>>>> f659b5a29b1f8d37ff19d9aa0d8226b6d0b6a333:code/test.py

motor = pwmio.PWMOut(board.GP14,duty_cycle = 65535,frequency=5000)

while (True):
<<<<<<< HEAD:raspberry-pi/test.py
    motor.duty_cycle = 4000
    print(board.GP10) #digital
    print(board.GP11) #analog
    print(board.GP12) #I2C
    print(board.GP13) #encoder
=======
    motor.duty_cycle = 40000
    print(board.GP10) #digital
    print(board.GP11) #analog
    print(board.GP12) #I2C
    print(board.GP13) #encoder
>>>>>>> f659b5a29b1f8d37ff19d9aa0d8226b6d0b6a333:code/test.py
