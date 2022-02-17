def unique(listed):
    unique = {}
    for i in listed:
        unique.update({i:"unique"})
    unique_elements = list(unique.keys())
    return unique_elements
txt = input("Enter your list of elements: ")
listed = txt.split(" ")
print(unique(listed))