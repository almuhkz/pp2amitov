print("a Python program to find the sequences of one upper case letter followed by lower case letters.")
import re
text = input("Enter your string: ")
expression = re.search('[A-Z]{1,}[a-z]+', text)
if expression:
  print("MATCH FOUND")
else:
  print("No match found.")
