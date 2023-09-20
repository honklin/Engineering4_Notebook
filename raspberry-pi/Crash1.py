#type: ignore
import time #delay library
import board #pins library
import adafruit_mpu6050 #accelerometer libary
import busio

i2c = busio.I2C(board.GP15, board.GP14) #I2C device declaration
mpu = adafruit_mpu6050.MPU6050(i2c) #accelerometer declaration

while True:
    print(mpu.acceleration) #accerelometer data
    time.sleep(.5)
