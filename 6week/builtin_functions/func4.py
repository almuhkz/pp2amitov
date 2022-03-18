from math import sqrt
from time import sleep
def sq_ml(x,m):
    res = sqrt(x)
    sleep(m/1000)
    return 'Square root of ' + str(x)+' after '+ str(m) +' miliseconds is '+str(res)
x = int(input())
m = int(input())
print(sq_ml(x,m))