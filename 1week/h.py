#Problem H: 187532. First and last occurrence.
s = str(input())
t = input()
j = s.count(t)
i = 0
l = []
for c in s:
    if c == t:
        l.append(i)
    i = i + 1
if j>1:
    print(l[0],l[-1])
else:
    print(l[0])