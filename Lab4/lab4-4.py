alternativ = 4
kör = True
def meny(alternativ):
# Definierar menyalternativen och returnerar alternativet (men returnerar False om användaren väljer avsluta)
    print("Välj ett av följande:")
    print("1. Ladda in data")
    print("2. Beräkna medelvärdet")
    print("3. Beräkna standardavvikelsen")
    print("4. Avsluta")

    while True:
        try:
            menyval = input("Val:")
            if 0 < int(menyval) <= alternativ:
                break
            else:
                print("Välj ett alternativ mellan 1 och ", alternativ)
        except ValueError:
            print(menyval, " är inte ett tal")

    if int(menyval) == alternativ:
        return False
    else:
        return int(menyval)

def tal_av_fil():
    # Frågar användaren efter en sökväg och returnerar filen via variabeln fil
    while True:
        sökväg = input("Ange filnamn: ")
        try:
            fil = open(sökväg, "r")
            break
        except FileNotFoundError:
            print("Filen "+sökväg+" kan inte hittas, försök igen!")
    ls = []
    for line in fil:
        if not line.startswith("#"):
            ls.append(int(line))
    print("Laddade in ", len(ls), " tal.")
    fil.close
    return ls

def medel(ls):
    # Returnerar medelvärdet av en lista utan att använda len eller sum
    summa, j = 0, 0
    for i in ls:
        summa += ls[j]
        j += 1
    return summa / j

import math


def standardavvikelse(datapunkter):
    # Räknar ut standardavvikelsen av punkterna i listan data
    summa = 0
    for i in range(len(datapunkter)):
        summa += math.pow((datapunkter[i] - (sum(datapunkter) / len(datapunkter))), 2)
    return math.sqrt( (1/(len(datapunkter)-1) )*summa)

while kör is not False:
    kör = meny(alternativ)
    if kör == 1:
        print("")
        tallista=tal_av_fil()
        print("")
    elif kör == 2:
        try:
            print("\nMedelvärdet är: ", medel(tallista), end="\n\n")
        except:
            print("\nDu måste välja en fil med tal innan du kan räkna ut medelvärdet", end="\n\n")
    elif kör == 3:
        try:
            print("\nStandardavvikelsen är: ", standardavvikelse(tallista), end="\n\n")
        except:
            print("\nDu måste välja en fil med tal innan du kan räkna ut medelvärdet", end="\n\n")
