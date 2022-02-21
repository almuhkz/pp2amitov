class Shape():
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        self.area = 0
        self.area = self.width * self.length
        print(self.area)
class Square(Shape):
    def __init__(self, length, width):
        super().__init__(length, width)
        
txt = int(input("Enter length: "))
figure = Square(txt, txt)
figure.area()
