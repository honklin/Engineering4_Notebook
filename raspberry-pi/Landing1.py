#type: ignore
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
                exit = False #restarts code by exiting all loops