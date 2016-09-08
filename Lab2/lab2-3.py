antal=int(input("Hur många tal vill du mata in? "))
tal=[]

#For-loopen skapar listan tal med bara de positiva talen
for i in range(1, antal+1, 1):
    tempVar=int(input("Ange tal %d: " %i))
    if tempVar>0: tal.append(tempVar)

print("\nSumman av de positiva talen blir %d." %sum(tal))
