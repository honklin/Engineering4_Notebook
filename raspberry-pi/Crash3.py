#type: ignore
import board #pins library
import digitalio #LED library
import adafruit_mpu6050 #accelerometer libary
import busio
from adafruit_display_text import label #text library
import adafruit_displayio_ssd1306 #OLED library
import terminalio #terminal library
import displayio #display library

displayio.release_displays() #starts display
i2c = busio.I2C(board.GP5, board.GP4) #I2C device declaration
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68) #accelerometer declaration

display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP2) #OLED i2c declaration
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64) #display declaration

led = digitalio.DigitalInOut(board.GP0) #LED declaration
led.direction = digitalio.Direction.OUTPUT


while True:
    splash = displayio.Group()
    title = "ANGULAR VELOCITY"
    text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5) #text settings
    text_area.text = f"{title}\n{round(mpu.gyro[0],3)},{round(mpu.gyro[1],3)},{round(mpu.gyro[2],3)}" #text to display
    splash.append(text_area) #adds text   
    display.show(splash) #displays text on OLED
    if (mpu.acceleration[2] < 2): #if board tilts
        led.value = True #turns led on
    else:
        led.value = False #turns led off otherwise