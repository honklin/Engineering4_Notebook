def check(test):
    try:
        print(test)
        return True
    except:
        print("Incorrect syntax - please re-enter:")
        return False

def area(x,y,z):
    x = x.split(",")
    y = y.split(",")
    z = z.split(",")
    x[0] = float(x[0])
    x[1] = float(x[1])
    y[0] = float(y[0])
    y[1] = float(y[1])
    z[0] = float(z[0])
    z[1] = float(z[1])
    a = x[0]*(y[1]-z[1])+y[0]*(z[1]-x[1])+z[0]*(x[1]-y[1])
    a = (1/2) * abs(a)
    return a

while True:
    exit = True
    print("Enter the first coordinate x,y:")
    x = input()
    while(check(x) and exit):
        print("Enter the second coordinate x,y:")
        y = input()
        while(check(y) and exit):
            print("Enter the third coordinate x,y:")
            z = input()
            if(check(z)):
                a = area(x,y,z)
                print("Area: ")
                print(a)
                exit = False