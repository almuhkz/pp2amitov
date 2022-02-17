import itertools
from math import factorial
def permutations(txt):
    chars = list(txt)
    permutations = list(itertools.permutations(chars))
    permutations_list = []
    for i in permutations:
        res = ""
        for j in i:
            res += j
        permutations_list.append(res)
    return permutations_list
txt = input("Enter your string here: ")
print("The amount of permutations of string " + txt + " is " + str(factorial(len(txt))))
print("Permutations for "+ txt +" are")
print(permutations(txt))

