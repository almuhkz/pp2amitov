def split_upper():
    import re
    print(" a Python program to split a string at uppercase letters and add them with space.")
    text = input("Enter your string: ")
    res = re.findall('[A-Z][^A-Z]*',text)
    result = ''
    for i in res:
        result+=i +" "
    print(result)
split_upper()