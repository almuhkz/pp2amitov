print("a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.")
import re
text = input("Enter your string: ")
expression = re.search('a.*b$', text)
if expression:
  print("MATCH FOUND")
else:
  print("No match found.")