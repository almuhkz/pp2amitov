class Strings():
    def __init__(self):
        pass
    def getString(self):
        self.txt = input()
    def printString(self):
        print(self.txt.upper())
text = Strings()
text.getString()
text.printString()