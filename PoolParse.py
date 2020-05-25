import os

CMain = {}
CExtra = {}
section = 0

def FileParse(fname, rarity):
    global section

    file = open(fname, 'r')
    lines = file.readlines()

    for line in lines:
        card = line.rstrip("\n")
        if card == "#main" or  card == "!side":
            section = 0
        elif card == "#extra":
            section = 1
        elif line[0].isdigit():
            switcher = CategorySwitch(rarity)
            InsertCardIntoCategory(card,switcher)

def CategorySwitch(rarity):
    argument = (rarity, section)
    switcher = {
        ("C",0):0,
        ("U",0):1,
        ("R",0):2,
        ("C",1):3,
        ("U",1):4,
        ("R",1):5,
    }

    return switcher.get(argument)

def InsertCardIntoCategory(card,switcher):

    if switcher == 0:
        if CMain.get(card) == None:
            CMain[card] = [1]
        else:
            CMain.get(card)[0] += 1
    elif switcher == 3:
        if CExtra.get(card) == None:
            CExtra[card] = [1]
        else:
            CExtra.get(card)[0] += 1



COMMON_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Common'))

comfiles = os.listdir(COMMON_DIR)

for file in comfiles:
    FileParse(os.path.join(COMMON_DIR,file),"C")

print(CMain)
print(CExtra)
