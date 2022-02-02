#Problem G: 195718. To decimal.
s = str(input())
res = 0
def todecimal(s,j,k):
    global res
    if(k == len(s)):
        return res
    if(s[j]=="0"):
        return todecimal(s,j-1,k+1)
    elif(s[j]=="1"):
        res += int(s[j])*(2**k)
        return todecimal(s,j-1,k+1)
j = -1 #index stringa
k = 0  #stepen dvoiki
print(todecimal(s,j,k))
#Urraaaa ya reshil




 
    