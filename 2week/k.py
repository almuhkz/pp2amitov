txt = input()
words=[]
list = txt.split(" ")
for x in list:
    c = x[-1]
    if(c.isalpha()==False):
        word = x
        c = len(x)-1
        words.append(word[0:c])
    if(x.isalpha()):
        words.append(x)
words.sort()
set1 = {"abc"}
set1.clear()
set1.update(words)
set = sorted(set1)
print(len(set))
for k in set:
    print(k)
