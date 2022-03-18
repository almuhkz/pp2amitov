def multiply(arr):  
    arr1= filter(lambda x: type(x)==type(1),arr)
    r = 1
    for i in arr1: r *= i
    return r  
print(multiply([1,2,3,'s','sssss',['a'],4,5,6]))


