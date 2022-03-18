def checkpalindrome(s):
    nstring = s.lower()
    if nstring == nstring[::-1]:
        return 'YES'
    else:
        return 'NO'
print(checkpalindrome(input("ENTER YOUR STRING HERE: ")))
