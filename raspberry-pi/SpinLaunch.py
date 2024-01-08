#type: ignore
import board
import time
import digitalio
import pwmio

motor = pwmio.PWMOut(board.GP14,duty_cycle = 65535,frequency=5000)

release = digitalio.DigitalInOut(board.GP1)
release.direction = digitalio.Direction.OUTPUT
release.value = True

led = digitalio.DigitalInOut(board.GP0)
led.direction = digitalio.Direction.OUTPUT
led.value = True

speed = 0
encoder = 0
encoderMax = 50
rotation = 0
rotationMax = 15

while (speed < 65535):
    motor.duty_cycle = speed
    print(speed)
    speed += 5
    time.sleep(.001)
while True:
    if (encoder == max):
        rotation += 1
        encoder = 0
    else:
        encoder = encoder
    if (encoder == encoderMax and rotation == rotationMax):
        release.value = False
        led.value = False
        while (speed > 0):
            speed -= 10
            time.sleep(.001)
        break