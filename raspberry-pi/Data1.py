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

with open("/data.csv", "a") as datalog:
    while True:
        runtime = time.monotonic()
        xacc = mpu.acceleration[0]
        yacc = mpu.acceleration[1]
        zacc = mpu.acceleration[2]
        led.value = True
        if (zacc < 5): #if board tilts
            tilt = True
        else:
            tilt = False
            time.sleep(.1)
            led.value = False
        datalog.write(f"{runtime},{xacc},{yacc},{zacc},{tilt}\n")
        datalog.flush()
        time.sleep(.25)