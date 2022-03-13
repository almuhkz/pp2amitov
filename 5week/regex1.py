print("a Python program that matches a string that has an 'a' followed by zero or more 'b''s.")
import re
text = input("Enter your string: ")
expression = re.search('ab*', text)
if expression:
  print("MATCH FOUND")
else:
  print("No match")
