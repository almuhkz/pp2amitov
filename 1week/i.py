#Problem I: 189327. Dimash that's too bad.
n = int(input())
i=0
m = []#mail
l = []
while i<n:
    m.append(str(input()))
    if(m[i].endswith("@gmail.com")):
        l.append(m[i])
    i+=1
for c in l:
    print(c.replace("@gmail.com",""))