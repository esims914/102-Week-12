
def PrintOutput(string):
    print("OUTPUT " + string)
    
def LoadFile(fileloc):
    f = open(fileloc)
    alist = []
    for line in f:
        alist.append(line)
    return alist
    f.close()

def UpdateString(string, char, pos):
    newstr = ''
    for i in range(pos):
        newstr += string[i]
    newstr += char
    for i in range(len(newstr)-1+len(char),len(string)):
        newstr += string[i]
    return newstr

def FindWordCount(alist,astr):
    numb = 0
    for i in range(len(astr)):
        alist += ' '
    for item in alist:
        letterloc = -1
        for letter in item:
            letterloc += 1
            if letter == astr[0]:
                tempcounter = 0
                for j in range(len(astr)):
                    if item[letterloc+j] != astr[j]:
                        break
                    else:
                        tempcounter += 1
                if tempcounter == len(astr):
                    numb += 1
    return numb
