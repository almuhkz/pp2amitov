import os
def onlyFiles(path):
    file_names = os.listdir(path)
    for fileName in file_names:
        if(os.path.isfile(os.path.join(path,fileName))):
            print('File Name: '+ fileName)
def onlyDirs(path):
    dir_names = os.listdir(path)
    for dirName in dir_names:
        if not(os.path.isfile(os.path.join(path,dirName))):
            print('Directory Name: '+ dirName)
def allFiles(path):
    file_names = os.listdir(path)
    for fileName in file_names:
        if(os.path.isfile(os.path.join(path,fileName))):
            print('File Name: '+ fileName)
        if not(os.path.isfile(os.path.join(path,fileName))):
            print('Directory Name: '+ fileName)
fol_path = r'C:\\Users\\amito\\OneDrive\Documents\\PP2'
onlyFiles(fol_path)
print('=========')
onlyDirs(fol_path)
print('=========')
allFiles(fol_path)