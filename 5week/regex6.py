print("a Python program to replace all occurrences of space, comma, or dot with a colon.")
import re
text = input("Enter your string: ")
expression = re.sub('[\s,.]',':', text)
print(expression)
