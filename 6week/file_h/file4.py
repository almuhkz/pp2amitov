def num_lines():
    with open(r"C:\\Users\\amito\\OneDrive\\Documents\\PP2\\6week\\file_h\\lines.txt", 'r') as f:
        counter = len(f.readlines())
        return ('Total lines:', counter)
print(num_lines())
''' with open(r"C:\\Users\\amito\\OneDrive\\Documents\\PP2\\6week\\file_h\\lines.txt", 'r') as f:
        counter = 0
        for line in f:
            if(line!=/n): counter +=1
        return ('Total lines:', counter)'''