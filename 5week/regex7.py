import re
print("a python program converts snake case string to camel case string.")
def snake_camel(match):
    return match.group(1) + match.group(2).upper()
txt = input("Enter your string: ")
finder = re.sub(r"(.*?)_([a-zA-Z])", snake_camel, txt)
print(finder)