#type: ignore
import time #delay library
import board #board library
import adafruit_mpu6050 #accelerometer library
import busio

sda = board.G14 #SDA pin
scl = board.G15 #SCL pin
i2c = busio.I2C(scl,sda) #I2C device declaration

mpu = adafruit_mpu6050.MPU6050(i2c) #accelerometer

while True:
    print(mpu.acceleration) #accelerometer output
    time.sleep(.5)
