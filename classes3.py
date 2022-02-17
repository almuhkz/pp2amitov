class Shape():
    area = 0
    def __init__(self):
      pass
    def area(self):
       self.area = 0
       print(self.area)
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length= length
        self.width=width
    def area(self):
        self.area = self.length * self.width
        return self.area
class Square(Shape):
    def __init__(self,length):
        self.length = length
    def area(self):
        self.area = self.length **2
        print(self.area)
txt = input("Enter length and width of Rectangle: ")
list = txt.split(" ")
figure = Rectangle(length=int(list[0]) , width=int(list[1]))
print(figure.area())
