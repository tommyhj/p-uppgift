antal=int(input("Hur många tal vill du mata in? "))
i=int(1)
tal=[]

#While-loopen skapar en lista som heter tal och som bara tar med de positiva talen som användaren skriver in
while i<=antal:
    tempVar=int(input("Ange tal %d: " %i)) 
    if tempVar>0: tal.append(tempVar)
    i=i+1
    
print("\nSumman av de positiva talen blir %d." %sum(tal))
