n = int(input())
i = 0
listed = []
dic = {}
while i<n:
    txt = input()
    list = txt.split(" ")
    name = str(list[0])
    pay = int(list[1])
    if name in dic:
        pay1 = dic.get(name)
        dic.pop(name)
        dic[name] = pay1 + pay
    else:
        dic.update({name: pay})
    i = i+1
maximum=max(dic.values())
for x,y in dic.items():
    if y != maximum:
        remain=maximum-y
        listed.append(x + " has to receive " + str(remain)+" tenge" )
    if y == maximum:
        listed.append(x + " is lucky!")
listed.sort()
for x in listed:
    print(x)