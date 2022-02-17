def spy_game(nums):
    str_nums = ""
    for i in nums:
        str_nums += str(i)
    length = len(str_nums)
    if(str_nums.find("0")!=-1):
        zero = str_nums.find("0")
        if(str_nums.find("0",zero+1,length)!=-1):
            zero2 = str_nums.find("0",zero+1)
            if(str_nums.find("7",zero2+1,length)!=-1):
                return True
    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))
print(spy_game([0,2,4,5,0,1,7]))
