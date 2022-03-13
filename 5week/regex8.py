def split_upper():
    import re
    print(" a Python program to split a string at uppercase letters.")
    text = input("Enter your string: ")
    print(re.findall('[A-Z][^A-Z]*',text))
split_upper()