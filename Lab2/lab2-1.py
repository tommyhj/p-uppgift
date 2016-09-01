#listan prisKlass innehåller prisklasserna för porto
prisKlass=[30, 28, 25, 24]

#porto-funktionen beräknar porto utifrån priserna i prisKlass och angiven vikt
def porto(vikt):
    if vikt<2:
        pris=prisKlass[0]
    elif vikt < 6:
        pris=prisKlass[1]
    elif vikt < 12:
        pris=prisKlass[2]
    else:
        pris=prisKlass[3]    
    return float(vikt)*pris


print("*"*20, "Portokalkyl", "*"*20, "\n")
print("Detta är ett program för att beräkna portokostnaden för paketförsändelser.\n")
vikt=float(input("Ange paketets vikt i kilo:\n"))

print("\nPaketets porto blir %.2f kr" %porto(vikt))

