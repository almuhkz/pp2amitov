n = int(input())
shelf = []
i = 0 
taken = []
while i<n:
    o = input()
    if(len(o)>1):
        list = o.split(" ")
    else: list[0] = o
    if(list[0]=="1"):
        shelf.append(list[1])
    if(list[0]=="2"):
        taken.append(shelf[0])
        shelf.pop(0)
    i = i + 1
res = ""
for x in taken:
    res = res + x + " "
print(res)