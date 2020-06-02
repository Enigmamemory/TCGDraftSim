import os
import json

import CardData as CD

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
            data = CD.Get_Card_Info(card)
            cardname = data["name"]
            InsertCardIntoCategory(cardname,switcher,data)

def InfoAdd(data):

    info = [1]

    type = data['type']
    ptype = CD.Parse_Type(type)

    islink = CD.Is_Link(ptype)
    ismon = CD.Is_Mon(ptype)
    ispend = CD.Is_Pend(ptype)

    race = data['race']
    desc = data['desc']

    if ismon:

        attribute = data['attribute']
        atk = data['atk']

        if islink:
            linkval = data['linkval']
            linkmarkers = ', '.join(data['linkmarkers'])

            info.append(type)
            info.append('Attribute: ' + attribute)
            info.append('Type: ' + race)
            info.append('Linkval: ' + str(linkval))
            info.append('Linkmarkers: ' + linkmarkers)
            info.append('Atk: ' + str(atk))
            info.append('Effect: ' + desc)

        else:

            defense = data['def']
            level = data['level']

            info.append(type)
            info.append('Level: ' + str(level))
            info.append('Attribute: ' + attribute)
            info.append('Type: ' + race)

            if ispend:
                scale = data['scale']
                info.append('Scale: ' + str(scale))

            info.append('Atk: ' + str(atk))
            info.append('Def: ' + str(defense))
            info.append('Effect: ' + desc)

    else:

        info.append(type)
        info.append('Type: ' + race)
        info.append('Effect: ' + desc)

    return info

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

def InsertCardIntoCategory(cardname,switcher,data):

    if switcher == 0:
        if CMain.get(cardname) == None:
            cardinfo = InfoAdd(data)
            CMain[cardname] = cardinfo
        else:
            CMain.get(cardname)[0] += 1
    elif switcher == 3:
        if CExtra.get(cardname) == None:
            cardinfo = InfoAdd(data)
            CExtra[cardname] = cardinfo
        else:
            CExtra.get(cardname)[0] += 1



COMMON_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Common'))

comfiles = os.listdir(COMMON_DIR)

for file in comfiles:
    FileParse(os.path.join(COMMON_DIR,file),"C")

print(CMain)
print(CExtra)
