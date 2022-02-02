#Problem F: 193526. Tears.
n = int(input())
wpw = []#workperweek
while n!=0:
    wpw.append(int(input()))
    n = n - 1
for i in wpw:
    if(i<=10):
       print("Go to work!") 
    elif(i>10 and  i<=25):
        print("You are weak")
    elif(i>25 and i<=45):
        print("Okay, fine")
    elif(i>45):
        print("Burn! Burn! Burn Young!")
