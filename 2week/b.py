x = input()
def toint(n):
    i = 0
    while i < len(n):
        n[i] = int(n[i])
        i = i+1
    return n
txt = input()
n = txt.split(" ")
nums=toint(n)
res = []
res.append(max(nums))
nums.remove(max(nums))
res.append(max(nums))
print(res[0]*res[1])

