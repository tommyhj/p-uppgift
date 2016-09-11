def multiTabell(rader, kolumner):
# Skriver ut en multiplikationstabell, rader*kolumner
    i = 0
    while i <= rader:
        j = 0
        while j <= kolumner:
            if i == 0 and j == 0:
                print("", end="\t")
            elif i == 0 and j == 1:
                
                k = 1
                while k <= kolumner:
                    print(k, end="\t")
                    k += 1
            elif i >= 1 and j < kolumner:
                print(i*(j+1), end="\t")
            j += 1
        i += 1
        print("")
        if i <= rader:
            print(i, "", end="\t")
rader = int(input("Ange antal rader:"))
kolumner = int(input("Ange antal kolumner:"))
multiTabell(rader, kolumner)
