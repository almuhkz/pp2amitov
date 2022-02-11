def year(e):
    return e['y']
def month(e):
    return e['m']
def day(e):
    return e['d']    
i = 1
list=[]
listed=[]
dic ={}
while i!=0:
    x = str(input())
    if(x == "0"):
        break
    list = x.split(" ",2)
    dic = {'d': list[0],
           'm': list[1],
           'y': list[2]}
    listed.append(dic)
listed.sort(key=day)
listed.sort(key=month)
listed.sort(key=year)
i = 0
while i<len(listed):
    h = listed[i]
    res = ""
    for g in h.values():
        res = res + g + " "
    print(res)
    i = i + 1
