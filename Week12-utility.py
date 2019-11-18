

def PrintOutput(string):
    print("OUTPUT " + string)
    
def LoadFile(fileloc):
    f = open(fileloc)
    alist = []
    for line in f:
        alist.append(line)
    print(alist)
    f.close()
