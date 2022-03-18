import os
def Files(path):
    exist = os.access(path,os.F_OK)
    readable = os.access(path, os.R_OK)
    writable = os.access(path, os.W_OK)
    executable = os.access(path, os.X_OK)
    print(path, ' EXISTENCE: ', exist)
    print(path, ' READABILITY: ', readable )
    print(path, ' WRITABILITY: ', writable )
    print(path, ' EXECUTABILITY :', executable )
fol_path = r'C:\\Users\\amito\\OneDrive\Documents\\PP2\\func1.py'
Files(fol_path)
print('=========')
