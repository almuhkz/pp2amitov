import random 
def guessnumber(name):
    print("Well, " + name + ", I am thinking of a number between 1 and 20.")
    number = random.randrange(1,21)
    print("Take a guess.")
    guess = int(input())
    tries = 1
    result = False
    while(result == False):
        if(guess<number):
            print("Your guess is too low.")
            print("Take a guess.")
            guess = int(input())
            tries += 1
        if(guess>number):
            print("Your guess is too high.")
            print("Take a guess.")
            guess = int(input())
            tries += 1
        if(guess==number):
            print("Good job, KBTU! You guessed my number in " + str(tries) +" guesses!")
            break
print("Hello! What is your name?")
name = input()
guessnumber(name)

'''Hello! What is your name?
KBTU

Well, KBTU, I am thinking of a number between 1 and 20.
Take a guess.
12

Your guess is too low.
Take a guess.
16

Your guess is too low.
Take a guess.
19

Good job, KBTU! You guessed my number in 3 guesses!'''