#type: ignore
import board #pins
import time #delay
import busio
from adafruit_display_shapes.triangle import Triangle #triangle
from adafruit_display_shapes.line import Line #line
from adafruit_display_shapes.circle import Circle #circle
import adafruit_displayio_ssd1306 #OLED library
from adafruit_display_text import label #text library
import displayio #display library

displayio.release_displays() #starts display
i2c = busio.I2C(board.GP5, board.GP4) #I2C device declaration
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP2) #OLED i2c declaration
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64) #display declaration


def check(test): #checks syntax
    try:
        test[0] = float(test[0]) #change to float
        test[1] = float(test[1])
        return test #return float
    except:
        print("Incorrect syntax - please re-enter using x,y syntax:") #prompt new value
        return False

def area(x,y,z): #calculate and return area
    return (1/2) * abs(x[0]*(y[1]-z[1])+y[0]*(z[1]-x[1])+z[0]*(x[1]-y[1]))

def graph(x,y,z): #draws graph and triangle
    splash = displayio.Group() #declares splash
    xaxis = Line(0,32,128,32, color=0xFFFF00) #draws x-axis
    splash.append(xaxis)
    yaxis = Line(64,0,64,64, color=0xFFFF00)
    splash.append(yaxis)
    origin = Circle(64,32,2,outline=0xFFFF00)
    splash.append(origin)
    triangle = Triangle(64+int(x[0]),32-int(x[1]),64+int(y[0]),32-int(y[1]),64+int(z[0]),32-int(z[1]),outline=0xFFFF00)
    splash.append(triangle)
    display.show(splash)

while True:
    exit = True #restarts loops
    print("Enter the first coordinate x,y:")
    x = input().split(",") #splits first coordinate
    while(check(x) != False and exit): # runs until correct syntax entered
        x = check(x) #saves float values
        print("Enter the second coordinate x,y:")
        y = input().split(",") #splits second coordinate
        while(check(y) != False and exit): #runs until correct syntax entered
            y = check(y) #saves float values
            print("Enter the third coordinate x,y:")
            z = input().split(",") #splits third coordinate
            if(check(z) != False): #runs until correct syntax entered
                z = check(z) #saves float values
                a = str(area(x,y,z)) #gets area value
                print("The area of the triangle with vertices ("+str(x[0])+", "+str(x[1])+"), ("+str(y[0])+", "+str(y[1])+"), ("+str(z[0])+", "+str(z[1])+") is "+a+" square km") #prints coordinates and area
                graph(x,y,z) #prints graph on OLED
                time.sleep(5) #waits to see graph
                exit = False #restarts code by exiting all loops