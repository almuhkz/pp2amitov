print("a Python program that matches a string that has an 'a' followed by two to three 'b'.")
import re
text = input("Enter your string: ")
expression = re.search('ab{2,3}', text)
if expression:
  print("MATCH FOUND")
else:
  print("No match found.")
