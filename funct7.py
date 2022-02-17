def has_33(nums):
    if(nums.count(3)<2):
        return False
    i = 1
    while i<len(nums):
        if(nums[i-1]==3 and nums[i]==3):
            return True
        i = i + 1
    return False
'''txt = input("Enter numbers: ")
splitter = txt.split(" ")
intnums = []
i = 0
while i<len(splitter): 
    intnums.append(int(splitter[i]))
    i += 1
print(has_33(intnums))
'''
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3])) 
print(has_33([3, 1, 3]))