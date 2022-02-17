def histogram(listed):
    histogram = ""
    for i in listed:
        histogram = ""
        for j in range(i):
            histogram += "*"
        print(histogram)
txt = input("Enter your list of elements: ")
listed = txt.split(" ")
intlist = []
for i in listed:
    intlist.append(int(i))
histogram(intlist)