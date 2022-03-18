with open("lines.txt",'r') as f:
    with open("copylines.txt", "w") as f1:
        for line in f:
            f1.write(line)