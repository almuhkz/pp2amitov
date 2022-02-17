from math import sqrt
class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show(self):
        print("Coordinates of the point are: x1 = "+str(self.x)+"; y1 = "+str(self.y))
    def move(self):
        self.x = input("Enter a new coordinate for x1 = ")
        self.y = input("Enter a new coordinate for y1 = ")
    def dist(self):
        x2 = input("Enter the coordinate for x2 = ")
        y2 = input("Enter the coordinate for y2 = ")
        a = (int(x2) - int(self.x))**2
        b = (int(y2) - int(self.y))**2
        distance = sqrt(a + b)
        print("The distance between x1y1 and x2y2 is "+ str(distance))
txt = input("Enter the coordinates for x1y1 = ")
list = txt.split(" ")
coordinates = Point(x = int(list[0]),y = int(list[-1]))
coordinates.show()
print("Changing the coordinates....")
coordinates.move()
print("Computing distance....")
coordinates.dist()

