#Problem J: Levy the cryptographer
msg = str(input())
words = []
words = msg.rsplit(" ")
i=0
while i<len(words):
    if(len(words[i])<3):
        words.pop(i)
    else:
        i = i + 1
res = ""
i=0
while i<len(words):
    res += words[i] + " "
    i = i+1
print(res)