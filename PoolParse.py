import os
import json

import CardData as CD

CMain = {}
CExtra = {}
UMain = {}
UExtra = {}
RMain = {}
RExtra = {}
section = 0
savechoice = [1,1,1,1,1,1]

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
    elif switcher == 1:
        if UMain.get(cardname) == None:
            cardinfo = InfoAdd(data)
            UMain[cardname] = cardinfo
        else:
            UMain.get(cardname)[0] += 1
    elif switcher == 2:
        if RMain.get(cardname) == None:
            cardinfo = InfoAdd(data)
            RMain[cardname] = cardinfo
        else:
            RMain.get(cardname)[0] += 1
    elif switcher == 3:
        if CExtra.get(cardname) == None:
            cardinfo = InfoAdd(data)
            CExtra[cardname] = cardinfo
        else:
            CExtra.get(cardname)[0] += 1
    elif switcher == 4:
        if UExtra.get(cardname) == None:
            cardinfo = InfoAdd(data)
            UExtra[cardname] = cardinfo
        else:
            UExtra.get(cardname)[0] += 1
    elif switcher == 5:
        if RExtra.get(cardname) == None:
            cardinfo = InfoAdd(data)
            RExtra[cardname] = cardinfo
        else:
            RExtra.get(cardname)[0] += 1

def SaveCards(choice):

    if choice[0] == 1:
        with open('CMain.json', 'w') as jdump:
            json.dump(CMain, jdump)

    if choice[1] == 1:
        with open('UMain.json', 'w') as jdump:
            json.dump(UMain, jdump)

    if choice[2] == 1:
        with open('RMain.json', 'w') as jdump:
            json.dump(RMain, jdump)

    if choice[3] == 1:
        with open('CExtra.json', 'w') as jdump:
            json.dump(CExtra, jdump)

    if choice[4] == 1:
        with open('UExtra.json', 'w') as jdump:
            json.dump(UExtra, jdump)

    if choice[5] == 1:
        with open('RExtra.json', 'w') as jdump:
            json.dump(RExtra, jdump)


COMMON_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Common'))
UNCOMMON_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Uncommon'))
RARE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Rare'))

comfiles = os.listdir(COMMON_DIR)
unfiles = os.listdir(UNCOMMON_DIR)
rarefiles = os.listdir(RARE_DIR)

print("Reading Common Cards")
for file in comfiles:
    print("Reading " + file)
    FileParse(os.path.join(COMMON_DIR,file),"C")
    print("Finished Reading " + file)

print("Reading Uncommon Cards")
for file in unfiles:
    print("Reading " + file)
    FileParse(os.path.join(UNCOMMON_DIR,file),"U")
    print("Finished Reading " + file)

print("Reading Rare Cards")
for file in rarefiles:
    print("Reading " + file)
    FileParse(os.path.join(RARE_DIR,file),"R")
    print("Finished Reading " + file)

SaveCards(savechoice)

#print(CMain)
#print(CExtra)
