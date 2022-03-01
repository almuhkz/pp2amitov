import math
def area(s,l):
    apothem = l/(2*(math.tan(math.radians(180/s))))
    perimeter = l * s
    area = (perimeter*apothem)/2
    print(area)
    return area
sides = int(input("Enter the number of sides: "))
side_length = int(input("Enter the length of a side: "))
print("The area of the polygon is: "+str(math.floor(area(sides,side_length))))