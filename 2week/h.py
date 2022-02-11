import math 
p = input()
corp = p.split(" ")
xp = int(corp[0])
yp = int(corp[1])
n = int(input())
i = 0
dic = {}
list = []
while i<n:
    txt = input()
    cors = txt.split(" ")
    x = int(cors[0])
    y = int(cors[1])
    pow1= pow((x-xp),2)
    pow2= pow((y-yp),2)
    point = math.sqrt(pow1+pow2)
    dic.update({point: txt})
    list.append(point)
    i = i + 1
list.sort()
i = 0
while i<len(list):
    print(dic.get(list[i]))
    i = i + 1

