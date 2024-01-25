#type: ignore
import time #delay library
import board #pins library
import digitalio #LED library
import adafruit_mpu6050 #accelerometer libary
import busio

led = digitalio.DigitalInOut(board.GP1) #LED declaration
led.direction = digitalio.Direction.OUTPUT

i2c = busio.I2C(board.GP15, board.GP14) #I2C device declaration
mpu = adafruit_mpu6050.MPU6050(i2c) #accelerometer declaration

with open("/data.csv", "a") as datalog: #creates data.csv file
    while True:
        runtime = time.monotonic() #total time
        xacc = mpu.acceleration[0] #x acceleration
        yacc = mpu.acceleration[1] #y acceleration
        zacc = mpu.acceleration[2] #z accleration
        if (zacc < 5): #if board tilts
            tilt = True #turn on led
        else: #if board flat
            tilt = False #blink led
            time.sleep(.1)
        led.value = tilt
        datalog.write(f"{runtime},{xacc},{yacc},{zacc},{tilt}\n") #write data
        datalog.flush() #push data to csv
        time.sleep(.25)