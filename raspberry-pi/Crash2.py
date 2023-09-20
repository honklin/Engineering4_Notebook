#type: ignore
import time #delay library
import board #pins library
import digitalio #LED library
import adafruit_mpu6050 #accelerometer libary
import busio

led = digitalio.DigitalInOut(board.GP0) #LED declaration
led.direction = digitalio.Direction.OUTPUT

i2c = busio.I2C(board.GP15, board.GP14) #I2C device declaration
mpu = adafruit_mpu6050.MPU6050(i2c) #accelerometer declaration

while True:
    if (mpu.acceleration[2] < 7): #if board tilts
        led.value = True #turns led on
    else:
        led.value = False #turns led off otherwise