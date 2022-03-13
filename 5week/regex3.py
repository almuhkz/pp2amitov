print("a Python program to find sequences of lowercase letters joined with a underscore.")
import re
text = input("Enter your string: ")
expression = re.search(r'(^[a-z]+_([a-z]+)$)', text)
if expression:
  print("MATCH FOUND")
else:
  print("No match found.")
