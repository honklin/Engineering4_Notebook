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
    a = (1/2)abs(x1(y2-y3)+x2(y3-y1)+x3(y1-y2))
    return a

while True:
    print("Enter the first coordinate x,y:")
    x = float(input())
    while(check(x)):
        print("Enter the second coordinate x,y:")
        y = float(input())
        while(check(y)):
            print("Enter the third coordinate x,y:")
            z = float(input())
            if(check(z)):
                a = area(x,y,z)