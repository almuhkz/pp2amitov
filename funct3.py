def solve(numheads, numlegs):
    if(numlegs%2!=0):
        print("No answer")
    if(numheads<=numlegs/2):
        rabbits = int((numlegs / 2) - numheads)
        chicken = int(numheads - rabbits)
        print("Number of rabbits is " + str(rabbits) +". Number of chickens is " + str(chicken))
    else:
         print("No answer")
heads = int(input("Enter the number of heads: "))
legs = int(input("Enter the number of legs: "))
solve(heads,legs)
solve(35,94)