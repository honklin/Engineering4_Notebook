#type: ignore
import time #delay library
import board #pins library
import digitalio #LED library
import adafruit_mpu6050 #accelerometer libary
import busio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio

displayio.release_displays()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP2)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

i2c = busio.I2C(board.GP15, board.GP14) #I2C device declaration
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)

led = digitalio.DigitalInOut(board.GP0) #LED declaration
led.direction = digitalio.Direction.OUTPUT


while True:
    if (mpu.acceleration[2] < 2): #if board tilts
        led.value = True #turns led on
    else:
        led.value = False #turns led off otherwise