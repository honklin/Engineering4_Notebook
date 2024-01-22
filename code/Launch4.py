#type: ignore
import time #sleep library
import board #pin library
import digitalio #led library
import pwmio #pwm library
from adafruit_motor import servo #servo library

red = digitalio.DigitalInOut(board.GP0) #red led declaration
red.direction = digitalio.Direction.OUTPUT
green = digitalio.DigitalInOut(board.GP1) # green led declaration
green.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP2) #button declaration
button.pull = digitalio.Pull.DOWN
button.direction = digitalio.Direction.INPUT


pwm = pwmio.PWMOut(board.GP3,duty_cycle=2**15,frequency=100) #servo declaration
servo = servo.Servo(pwm)
servo.angle = 0

while True:
    if (button.value): #when button is pressed
        for i in range(10,0,-1): #counts down from 10
            print(i) #prints count
            red.value = True #red led on
            time.sleep(.5)
            red.value = False #red led off
            time.sleep(.5)
        print("Liftoff!")
        green.value = True #green led on
        servo.angle = 180 # turn servo
        time.sleep(10)