import os
def Files(path):
    exist = os.access(path,os.F_OK)
    if(exist):
        print('PATH EXISTS')
        print('PATH FILENAME IS: ',  os.path.basename(path))
        print('PATH DIRECTORY IS: ', os.path.dirname(path))
        os.remove(path)
        print('PATH DELETED SUCCESSFULLY')
    else:
        print(path, " PATH DOESNT EXIST")
fol_path = r'C:\\Users\\amito\\OneDrive\Documents\\PP2\\a.cpp'
Files(fol_path)
print('=========')
