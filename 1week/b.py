#Problem B: 196111. Boris the Chef.
S = input()
sum = 0
for c in S:
    sum += ord(c)
if (sum>300):
        print("It is tasty!")
else:
        print("Oh, no!")
