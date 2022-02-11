txt = input()
x = txt.split("+",1)
def splitstr(number):
    j = 0
    list = []
    while j!=len(number):
     word=number[j:j+3]
     list.append(word) 
     j = j+3
    return list
g = splitstr(x[0])
h = splitstr(x[1])
def convert(g,h):
    dic={
        "ZER": "0",
        "ONE": "1",
        "TWO": "2",
        "THR": "3",
        "FOU": "4", 
        "FIV": "5",  
        "SIX": "6", 
        "SEV": "7", 
        "EIG": "8", 
        "NIN": "9",
        "0": "ZER",
         "1":"ONE",
        "2": "TWO",
        "3":"THR",
         "4":"FOU", 
         "5":"FIV",  
         "6":"SIX", 
         "7":"SEV", 
        "8":"EIG", 
        "9": "NIN" 
    }
    res1 =""
    res2 =""
    for z in g:
        res1 = res1 + dic.get(z)
    for z in h:
        res2 = res2 + dic.get(z)
    res = int(res1)+int(res2)
    fres=str(res)
    finres = ""
    for z in fres:
        finres=finres+dic.get(z)
    return finres
print(convert(g,h))