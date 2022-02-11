i = 1
list=[]
while i!=0:
    x = input()
    if(x == "0"):
        break
    list.append(int(x))
finsum = ""
g=int(len(list))
g1=int(g/2)
i = 0
while i!=g1:
    sum = list[i] + list[-i-1]
    finsum = finsum  +str(sum) + " "
    i = i + 1
g3=round(g1)
if(g%2!=0):
    finsum = finsum + str(list[g3])
print(finsum)