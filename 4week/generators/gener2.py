def even(n):
    num = 0
    while num <= n:
        if(num%2==0):
            yield num
        num += 1
n = int(input("ENTER YOUR N: "))
res,txt = even(n),""
for i in res:
    txt += str(i)+ ", "
print(txt[0:-2]) 
"""
n = int(input("ENTER YOUR N: "))
gen_even = (x * 2 for x in range(int(n/2+1)))
txt = ""
for i in gen_even:
    txt += str(i)+ ", "
print(txt[0:-2]) 


"""
"""class Iterator:
  def __init__(self,n):
    self.current = 0
    self.n = n
    self.step = step
  def __iter__(self):
    yield self
  def __next__(self):
    if self.current <= self.n:
        res = self.current
        self.current += 2
        yield res
    else:
        raise StopIteration
n = int(input("ENTER YOUR NUMBER N: "))
evens = Iterator(n)
iter = iter(evens)
print(iter)
txt = ""
for x in iter:
    txt += str(x)+ ", "
print(txt[0:-2]) """