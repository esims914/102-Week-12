#   https://github.com/esims914/102-Week-12
#   Eugene (Trey) Sims
#   ​CSCI 102 – Section E
#   Week 11 - Part A


# Print Output
def PrintOutput(string):
    print("OUTPUT " + string)

# Load File
def LoadFile(fileloc):
    f = open(fileloc)
    alist = []
    for line in f:
        alist.append(line)
    return alist
    f.close()

# Update String
def UpdateString(string, char, pos):
    newstr = ''
    for i in range(pos):
        newstr += string[i]
    newstr += char
    for i in range(len(newstr)-1+len(char),len(string)):
        newstr += string[i]
    return newstr

# Find Word Count
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

# Score Finder
def ScoreFinder(playerlist, scorelist, player):
    found = False
    loc = -1
    for playername in playerlist:
        loc += 1
        if playername.upper() == player.upper():
            found = True
            print("OUTPUT " + playername + " got a score of " + str(scorelist[loc]))
            break
    if found == False:
        print("OUTPUT player not found")

        
            
