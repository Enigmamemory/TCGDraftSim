import json
import pprint
import random
import sys

CMain = {}
UMain = {}
RMain = {}
CExtra = {}
UExtra = {}
RExtra = {}

with open("CMain.json", "r") as read_file:
    CMain = json.load(read_file)

with open("UMain.json", "r") as read_file:
    UMain = json.load(read_file)

with open("RMain.json", "r") as read_file:
    RMain = json.load(read_file)

with open("CExtra.json", "r") as read_file:
    CExtra = json.load(read_file)

with open("UExtra.json", "r") as read_file:
    UExtra = json.load(read_file)

with open("RExtra.json", "r") as read_file:
    RExtra = json.load(read_file)

Main = {**CMain,**UMain,**RMain}
Extra = {**CExtra,**UExtra,**RExtra}

for card in UMain:
    if card in CMain.keys():
        print("Duplicate found between CMain and UMain")
        print(card)

for card in RMain:
    if card in CMain.keys():
        print("Duplicate found between CMain and RMain")
        print(card)
    if card in UMain.keys():
        print("Duplicate found between UMain and RMain")
        print(card)

for card in UExtra:
    if card in CExtra.keys():
        print("Duplicate found between CExtra and UExtra")
        print(card)

for card in RExtra:
    if card in CExtra.keys():
        print("Duplicate found between CExtra and RExtra")
        print(card)
    if card in UExtra.keys():
        print("Duplicate found between UExtra and RExtra")
        print(card)


CMainCount = 0
UMainCount = 0
RMainCount = 0
MainCount = 0
CExtraCount = 0
UExtraCount = 0
RExtraCount = 0
ExtraCount = 0

for card in CMain:
    CMainCount += CMain[card][0]

for card in UMain:
    UMainCount += UMain[card][0]

for card in RMain:
    RMainCount += RMain[card][0]

for card in Main:
    MainCount += Main[card][0]

for card in CExtra:
    CExtraCount += CExtra[card][0]

for card in UExtra:
    UExtraCount += UExtra[card][0]

for card in RExtra:
    RExtraCount += RExtra[card][0]

for card in Extra:
    ExtraCount += Extra[card][0]


print([CMainCount,UMainCount,RMainCount,MainCount,CExtraCount,UExtraCount,RExtraCount,ExtraCount])

settings = {}

with open("settings.txt", "r") as read_file:
    for line in read_file:
        s = line.strip("\n").split(":")
        settings[s[0]] = s[1]

def SealedPacks(settings):

    packs = 0

    packnum = int(settings["packs"])
    epacknum = int(settings["extrapacks"])

    total = int(settings["commons"]) + int(settings["uncommons"]) + int(settings["rares"])
    etotal = int(settings["ecommons"]) + int(settings["euncommons"]) + int(settings["erares"])

    poolsize = packnum * (total)
    epoolsize = epacknum * (etotal)

    poolnum = 0
    epoolnum = 0

    if poolsize % 60 != 0:
        poolnum += 1
    if epoolsize % 30 != 0:
        epoolnum += 1

    poolnum += poolsize // 60
    epoolnum += epoolsize // 30

    ydknum = max(poolnum,epoolnum)

    ydknames = []

    count = 0

    while count < ydknum:
        ydkname = "SealedCards{}.ydk".format(count)
        ydknames.append(ydkname)
        count += 1

    print(ydknames)

    seedValue = random.randrange(sys.maxsize)

    random.seed(seedValue)
    print("Seed was: {}".format(seedValue))

    playercards = {}
    playerextras = {}

    counter = 0

    while packs < packnum:

        c = 0
        u = 0
        r = 0

        if int(settings["random"]) == 0:
            while c < int(settings["commons"]):
                card = random.choice(list(CMain.items()))
                if playercards.get(card[0]) == None:
                    playercards[card[0]] = card[1]
                else:
                    playercards.get(card[0])[0] += 1
                CMain.get(card[0])[0] -= 1
                if CMain.get(card[0])[0] == 0:
                    CMain.pop(card[0])
                counter += 1
                c+=1
            while u < int(settings["uncommons"]):
                card = random.choice(list(UMain.items()))
                if playercards.get(card[0]) == None:
                    playercards[card[0]] = card[1]
                else:
                    playercards.get(card[0])[0] += 1
                UMain.get(card[0])[0] -= 1
                if UMain.get(card[0])[0] == 0:
                    UMain.pop(card[0])
                counter += 1
                u+=1
            while r < int(settings["rares"]):
                card = random.choice(list(RMain.items()))
                if playercards.get(card[0]) == None:
                    playercards[card[0]] = card[1]
                else:
                    playercards.get(card[0])[0] += 1
                RMain.get(card[0])[0] -= 1
                if RMain.get(card[0])[0] == 0:
                    RMain.pop(card[0])
                counter += 1
                r+=1

        else:
            while c < total:

                c+=1

        packs += 1

    print(len(playercards))
    print(counter)

    return 0

SealedPacks(settings)
