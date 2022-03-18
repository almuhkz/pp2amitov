def upper_lower(s):
    arr = list(s)
    upper = 0
    lower = 0
    for i in arr:
        if(65<=ord(i)<=90): upper+=1
        if(97<=ord(i)<=122): lower+=1
    return print("Number of uppercase letters are: " + str(upper)+", Number of lowercase letters are: "+ str(lower)) 
txt = input("Enter your string here: ")
upper_lower(txt)