n = int(input())#demon number
i = 0
dicd ={}#dictionary for demon
dic = {}#dict for slayer
while i < n:
    txt = input()
    list = txt.split(" ")
    weak = str(list[1])
    am = 1
    if weak in dicd:
        pay1 = dicd.get(weak)
        dicd.pop(weak)
        dicd[weak] = pay1 + am
    else:
        dicd.update({list[1]: am})
    i = i + 1
m = int(input())#slayer number
i = 0
while i < m:
    txt = input()
    list = txt.split(" ")
    pow = str(list[1])
    amo = int(list[2])
    if pow in dic:
        pay1 = dic.get(pow)
        dic.pop(pow)
        dic[pow] = pay1 + amo
    else:
        dic.update({list[1]: amo})
    i = i + 1
for x,y in dic.items():
    if x in dicd:
        remain= dicd.get(x) - y
        dicd.pop(x)
        dicd[x] = remain
demonleft = 0
newlist = dicd.values()
for x in newlist:
    if(x>0):
        demonleft = demonleft + x
print("Demons left: " + str(demonleft))