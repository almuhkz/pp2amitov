import math
def ispalindrome(splitted):
    words = []
    if(len(splitted)==1):
        result = False
        word = splitted[0]
        if(len(word)%2!=0):
            mid = math.floor(len(word)/2)
            for i in range(mid):
                if(word[i]==word[-i-1]):
                    result = True
        return result
    if(len(splitted)>1):
        j = 0
        while j < len(splitted): 
            word = splitted[j]
            for i in word:
                words.append(i)
            j = j + 1
        palindrome = words.copy()
        palindrome.reverse()
        if(words==palindrome):
            return True
    return False
phrase = input()
splitted = phrase.split(" ")
print(ispalindrome(splitted))
    

