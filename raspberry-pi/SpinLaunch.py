#type: ignore
import board
import time
import digitalio
import busio
import pwmio
import adafruit_mpu6050

i2c = busio.I2C(board.GP5, board.GP4)
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)
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
        rotations += 1
        encoder = 0
    else:
        encoder = encoder
    if (encoder == encoderMax and rotation == rotationMax):
        release.value = False
        led.value = False
        break