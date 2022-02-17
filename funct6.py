def reversed(splitter):
    result = ""
    splitter.reverse()
    i = 0
    while i<len(splitter):
        result = result + str(splitter[i]) + " "
        i = i + 1
    return result
txt = input("Enter your words: ")
splitter = txt.split(" ")
print(reversed(splitter))
