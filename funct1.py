def toOunce(grams):
    ounces = grams/28.3495231 
    return ounces
grams = int(input("Enter the amount of grams: "))
print(toOunce(grams))