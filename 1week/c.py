#Problem C: 187587. To Lowercase.
s = str(input())
def toLowercase(s):
    for c in s:
        char = ord(c)
        if 65<=char and char<=95:
            g = ord(c)+32
            s = s.replace(c , chr(g))
    return s
print(toLowercase(s))
#cpy ahaha
#ili prosto print(s.lower())