def num_lines(path,arr):
    with open(path, 'a') as f:
        for i in arr:
            f.write(i)
            f.write('\n')
file = r"C:\\Users\\amito\\OneDrive\\Documents\\PP2\\6week\\file_h\\lines.txt"
arr = ['Axe','Computer','Glasses']
num_lines(file,arr)
with open(file,'r') as f:
    print(f.read())
