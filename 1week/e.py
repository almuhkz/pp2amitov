#Problem E: 188812. Gunner.
l = input()
l = l.rsplit(" ", 1)
n = int(l[0])
f = int(l[1])
#is prime number check
prime = True
i = 2 #primedivisors
nr = n ** 1/2
while (i < nr):
    if(n%i==0):
        prime = False
        break
    else:
        i += 1
if((n<=500) and (prime==True) and (f%2==0)):
   print("Good job!")
else:
    print("Try next time!")