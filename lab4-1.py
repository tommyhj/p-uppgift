def filsökväg():
    # Frågar användaren efter en sökväg och returnerar filen via variabeln fil
    while True:
        sökväg = input("Ange filnamn: ")
        try:
            fil = open(sökväg, "r")
            break
        except:
            print("Filen "+sökväg+" kan inte hittas, försök igen!")
    return(fil)

textfil=filsökväg()
ls = []
for line in textfil:
    if not line.startswith("#"):
        ls.append(int(line))
print (ls)