import re
print("a python program converts camel case string to snake case string.")
def camel_snake(match):
    return match.group(1).lower() +"_"+ match.group(2).lower()
txt = input("Enter your string: ")
finder = re.sub(r"(.+?)([A-Z])", camel_snake, txt)
print(finder)