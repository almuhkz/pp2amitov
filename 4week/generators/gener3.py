def func(n):
    def div34(n):
        num = 0
        while num < n:
            num += 1
            if(num % 3 == 0 and num % 4 == 0):
                yield num
    res = div34(n)
    for i in res:
        print(i)
func(140)



