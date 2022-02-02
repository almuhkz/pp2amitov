#Problem D: 186885. Asman + Systems = Astems
x = int(input())
z = input()
if (z=="k"):
    x = float(x)
    c = int(input())
    if (x%1024!=0):
        x = x / 1024
        x = round(x,c)
    if (x%1024==0):
        x = x / 1024
        x = str(x)
        d = 1
        while d!=c:
            x = x + "0"
            d = d + 1
    print(x)
if (z=="b"):
    x *= 1024
    print(x)
#if (type(x) is not int):
#    c = int(input())