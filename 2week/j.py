n = int(input())
i = 0
strong = []
while i<n:
    txt = input()
    upper = False
    lower = False
    numbers = False
    chars = list(txt)
    i = i + 1
    for x in chars:
        if x.islower(): 
            lower = True
        if x.isnumeric():
            numbers = True
        if x.isupper():
            upper = True
    if(lower and numbers and upper):
        if txt in strong:
            continue
        else:
            strong.append(txt)

print(len(strong))
strong.sort()
for x in strong:
    print(x)