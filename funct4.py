def prime(number):
   prime = True
   isprime = lambda x,y: x % y ==0
   for i in range(2,number):
        if(isprime(number,i)):
            prime = False
            break
   return prime
def prime_filter(intlist):
    list_prime = list(filter(prime,intlist))
    return list_prime
txt = input("Enter the numbers: ")
intlist = []
splitter = txt.split(" ")
for x in splitter:
    intlist.append(int(x))
print(prime_filter(intlist))