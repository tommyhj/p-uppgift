#porto-funktionen beräknar portot utifrån 4 prisklasser som beror på vikt
def porto(vikt):
    if vikt<2:
        prisKlass=30
    elif vikt < 6:
        prisKlass=28
    elif vikt < 12:
        prisKlass=25
    else:
        prisKlass=23    
    return float(vikt)*prisKlass

print("*"*20, "Portokalkyl", "*"*20, "\n")
print("Detta är ett program för att beräkna portokostnaden för paketförsändelser.\n")
vikt=float(input("Ange paketets vikt i kilo:\n"))

print("\nPaketets porto blir %.2f kr" %porto(vikt))
