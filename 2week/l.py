txt = input()
string = txt.split(" ")
list = []
for j in string:
    list.append(int(j))
jumpmax = 0
canjump = 0  
for i in range(len(list)):
    if i > jumpmax:
        canjump = False
    jumpmax = max(jumpmax,i+list[i])
    canjump = True   
print(canjump)