import math
def Volume(radius):
    pi = math.pi
    volume = (4/3)*pi*(radius**3)
    return volume
radius = int(input("Enter the radius of a sphere: "))
print(Volume(radius))

