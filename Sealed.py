import json
import pprint
import random
import sys
import operator

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

    packs = 0

    while packs < packnum:

        c = 0
        u = 0
        r = 0

        if int(settings["random"]) == 0:
            while c < int(settings["commons"]):
                card = random.choice(list(CMain.items()))
                if playercards.get(card[0]) == None:
                    infocopy = card[1].copy()
                    infocopy[0] = 1
                    playercards[card[0]] = infocopy
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
                    infocopy = card[1].copy()
                    infocopy[0] = 1
                    playercards[card[0]] = infocopy
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
                    infocopy = card[1].copy()
                    infocopy[0] = 1
                    playercards[card[0]] = infocopy
                else:
                    playercards.get(card[0])[0] += 1
                RMain.get(card[0])[0] -= 1
                if RMain.get(card[0])[0] == 0:
                    RMain.pop(card[0])
                counter += 1
                r+=1

        else:
            while c < total:
                card = random.choice(list(Main.items()))
                if playercards.get(card[0]) == None:
                    infocopy = card[1].copy()
                    infocopy[0] = 1
                    playercards[card[0]] = infocopy
                else:
                    playercards.get(card[0])[0] += 1
                Main.get(card[0])[0] -= 1
                if Main.get(card[0])[0] == 0:
                    Main.pop(card[0])
                counter += 1
                c+=1

        packs += 1


    epacks = 0
    ecounter = 0

    #print(random.choice(list(CExtra.items())))

    while epacks < epacknum:

        c = 0
        u = 0
        r = 0

        if int(settings["random"]) == 0:
            while c < int(settings["ecommons"]):
                card = random.choice(list(CExtra.items()))
                if playerextras.get(card[0]) == None:
                    infocopy = card[1].copy()
                    infocopy[0] = 1
                    playerextras[card[0]] = infocopy
                else:
                    playerextras.get(card[0])[0] += 1
                CExtra.get(card[0])[0] -= 1
                if CExtra.get(card[0])[0] == 0:
                    CExtra.pop(card[0])
                ecounter += 1
                c+=1

            while u < int(settings["euncommons"]):
                card = random.choice(list(UExtra.items()))
                if playerextras.get(card[0]) == None:
                    infocopy = card[1].copy()
                    infocopy[0] = 1
                    playerextras[card[0]] = infocopy
                else:
                    playerextras.get(card[0])[0] += 1
                UExtra.get(card[0])[0] -= 1
                if UExtra.get(card[0])[0] == 0:
                    UExtra.pop(card[0])
                ecounter += 1
                u+=1
            while r < int(settings["erares"]):
                card = random.choice(list(RExtra.items()))
                if playerextras.get(card[0]) == None:
                    infocopy = card[1].copy()
                    infocopy[0] = 1
                    playerextras[card[0]] = infocopy
                else:
                    playerextras.get(card[0])[0] += 1
                RExtra.get(card[0])[0] -= 1
                if RExtra.get(card[0])[0] == 0:
                    RExtra.pop(card[0])
                ecounter += 1
                r+=1

        else:
            while c < etotal:
                card = random.choice(list(Extra.items()))
                if playerextras.get(card[0]) == None:
                    infocopy = card[1].copy()
                    infocopy[0] = 1
                    playerextras[card[0]] = infocopy
                else:
                    playerextras.get(card[0])[0] += 1
                Extra.get(card[0])[0] -= 1
                if Extra.get(card[0])[0] == 0:
                    Extra.pop(card[0])
                counter += 1

                c+=1

        epacks += 1

    '''
    print(len(playercards))
    print(counter)
    print(len(playerextras))
    print(ecounter)
    '''

    #print(playerextras)

    return (playercards,playerextras,ydknames,seedValue)

def PrintFiles(pcards,pextras,ydknames,seedValue):
    sortmain = sorted(pcards.items(), key=lambda i: i[1][0])
    sortextra = sorted(pextras.items(), key=lambda i: i[1][0])

    with open("sealedlog.txt","w") as f:
        f.write("Seed Value: ")
        f.write(str(seedValue))
        f.write('\n')
        f.write("Main Deck:\n")
        f.write("\n")
        for card in sortmain:
            string = str(card[1][0]) + "x " + str(card[0]) + "\n"
            f.write(string)
        f.write("\n")
        f.write("Extra Deck:\n")
        f.write("\n")
        for card in sortextra:
            string = str(card[1][0]) + "x " + str(card[0]) + "\n"
            f.write(string)

    ydkcount = 0

    while ydkcount < len(ydknames):

        maincount = 0
        sidecount = 0
        extracount = 0

        with open(ydknames[ydkcount], "w") as ydk:

            ydk.write("#created by ...\n")
            ydk.write("#main\n")

            mainiter = len(sortmain) - 1

            while maincount < 60 and len(sortmain) > 0:

                dupes = []

                if mainiter < 0:
                    mainiter = len(sortmain) - 1

                deposit = 0

                card = sortmain[mainiter]

                if card[0] not in dupes:
                    if maincount + card[1][0] > 60:
                        deposit = 60 - maincount
                    elif card[1][0] > 3:
                        deposit = 3
                        dupes.append(card[0])
                    else:
                        deposit = card[1][0]

                if deposit != 0:
                    ydk.write((str(card[1][1]) + '\n')*deposit)

                card[1][0] -= deposit
                if card[1][0] == 0:
                    sortmain.pop(mainiter)
                mainiter -= 1

                maincount += deposit

            ydk.write("#extra\n")

            sideiter = len(sortextra) - 1

            while extracount < 15 and len(sortextra) > 0:

                dupes = []

                if sideiter < 0:
                    sideiter = len(sortextra) - 1

                deposit = 0

                card = sortextra[sideiter]

                if card[0] not in dupes:
                    if sidecount + card[1][0] > 15:
                        deposit = 15 - sidecount
                    elif card[1][0] > 3:
                        deposit = 3
                        dupes.append(card[0])
                    else:
                        deposit = card[1][0]

                ydk.write((str(card[1][1]) + '\n')*deposit)

                card[1][0] -= deposit
                if card[1][0] == 0:
                    sortextra.pop(sideiter)
                sideiter -= 1

                extracount += deposit

            ydk.write("!side\n")

            sideiter = len(sortextra) - 1

            while sidecount < 15 and len(sortextra) > 0:

                dupes = []

                if sideiter < 0:
                    sideiter = len(sortextra) - 1

                deposit = 0

                card = sortextra[sideiter]

                if card[0] not in dupes:
                    if sidecount + card[1][0] > 15:
                        deposit = 15 - sidecount
                    elif card[1][0] > 3:
                        deposit = 3
                        dupes.append(card[0])
                    else:
                        deposit = card[1][0]

                ydk.write((str(card[1][1]) + '\n')*deposit)

                card[1][0] -= deposit
                if card[1][0] == 0:
                    sortextra.pop(sideiter)
                sideiter -= 1

                sidecount += deposit

        ydkcount += 1

    if len(sortmain) != 0:
        print("Warning: main deck cards not in ydk files:")
        for card in sortmain:
            print([card[0],card[1][0]])

    if len(sortextra) != 0:
        print("Warning: extra deck cards not in ydk files:")
        for card in sortextra:
            print([card[0],card[1][0]])

info = SealedPacks(settings)
PrintFiles(info[0],info[1],info[2],info[3])
