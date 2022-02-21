class Shape():
    def __init__(self, length,width):
        self.length = length
        self.width = width
    def area(self):
       self.area = 0
       self.area = self.length * self.width
       print(self.area)
class Rectangle(Shape):
    def __init__(self,length,width):
        super().__init__(length, width)
class Square(Shape):
   def __init__(self,length,width):
        super().__init__(length, width)
    
txt = input("Enter length and width of Rectangle: ")
list = txt.split(" ")
figure = Rectangle(length=int(list[0]) , width=int(list[1]))
figure.area()
