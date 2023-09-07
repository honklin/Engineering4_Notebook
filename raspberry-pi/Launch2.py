#type: ignore
import time
import board
import digitalio

red = digitalio.DigitalInOut(board.GP0)
red.direction = digitalio.Direction.OUTPUT
green = digitalio.DigitalInOut(board.GP1)
green.direction = digitalio.Direction.OUTPUT


for i in range(10,0,-1):
    print(i)
    red.value = True
    time.sleep(.5)
    red.value = False
    time.sleep(.5)

print("Liftoff!")
green.value = True
time.sleep(1)