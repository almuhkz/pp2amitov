def area(h,a,b):
    return (a+b)*h/2
height = int(input("Height value: "))
base_a = int(input("First base value: "))
base_b = int(input("Second base value: "))
print("The area of Trapezoid is: "+str(area(height,base_a,base_b)))
