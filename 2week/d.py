def prin(list):
    txt = ""
    for j in list:
        txt = txt + j 
    return txt
n = int(input())
i = 0
nh = n
tsu = []
nh = 0
for j in range(n):
        tsu.append(".")
while nh < n:
        tsu[-nh-1] = "#"
        nh = nh + 1
        if(n % 2 == 1):
            print(prin(tsu))
        if(n%2==0):
            tsu1 = tsu.copy()
            tsu1.sort()
            print(prin(tsu1))
       