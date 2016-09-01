def pris(vikt, pklass):        
        return float(vikt)*int(pklass)
print("*"*20, "Portokalkyl", "*"*20, "\n")
print("Detta är ett program för att beräkna portokostnaden för paketförsändelser.\n")
vikt=float(input("Ange paketets vikt i kilo:\n"))
if vikt<2:
        pklass=30
elif vikt < 6:
        pklass=28
elif vikt < 12:
        pklass=25
else:
        pklass=23

print("\nPaketets porto blir %.2f kr" %pris(vikt, pklass))
