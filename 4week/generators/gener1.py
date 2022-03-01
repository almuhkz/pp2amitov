def squares(current, n):
    while current <= n:
        yield current**2
        current += 1
res = squares(1, 10)
for i in res:
    print(i)
"""class Iterator:
  def __init__(self,number):
    self.number = number
  def __iter__(self):
    self.n = 1
    return self
  def __next__(self):
    if self.n <= self.number:
        res = self.n**2 
        self.n += 1
        return res
    else:
        raise StopIteration
#n = int(input("ENTER YOUR NUMBER N: "))
squares = Iterator(3)#enter your n here
iter = iter(squares)
for x in iter:
    print(x)
"""