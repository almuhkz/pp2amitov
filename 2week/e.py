def toint(n):
    i = 0
    while i < len(n):
        n[i] = int(n[i])
        i = i+1
    return n
txt = input()
if(txt.count(" ")==1):
    n = txt.split(" ")
    nums=toint(n)
    list=[]
    i = 0
    while (i<nums[0]):
        list.append(nums[1]+2*i)
        i = i+1
    i = 1
    res = list[0]
    while(i<len(list)):
        res = res^list[i]
        i = i + 1
    print(res)
else:
    txt2 = input()
    nums=[]
    nums.append(int(txt))
    nums.append(int(txt2))
    list=[]
    i = 0
    while (i<nums[0]):
        list.append(nums[1]+2*i)
        i = i+1
    i = 1
    res = list[0]
    while(i<len(list)):
        res = res^list[i]
        i = i + 1
    print(res)

