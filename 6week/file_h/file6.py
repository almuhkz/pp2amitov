def a_zfiles():
    for i in range(65,91,1):
        name = '{}.txt'
        with open(name.format(chr(i)), 'a') as f:
            f.write(chr(i))
a_zfiles()