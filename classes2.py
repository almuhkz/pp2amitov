class Shape():
    def __init__(self):
        pass
    def area(self):
        self.area = 0
        print(self.area)
class Square(Shape):
    def __init__(self,length):
        self.length = length
    def area(self):
        self.area = self.length **2
        print(self.area)
txt = int(input())
figure = Square(txt)
figure.area()


 