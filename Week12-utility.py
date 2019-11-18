

def PrintOutput(string):
    print("OUTPUT " + string)
    
def LoadFile(fileloc):
    f = open(fileloc)
    alist = []
    for line in f:
        alist.append(line)
    print(alist)
    f.close()

def UpdateString(string, char, pos):
    newstr = ''
    for i in range(pos):
        newstr += string[i]
    newstr += char
    for i in range(len(newstr)-1+len(char),len(string)):
        newstr += string[i]
    PrintOutput(newstr)
