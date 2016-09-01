#Funktionen aboveZero utvärderar varje position i listan ls och returnerar de värden som är positiva
def aboveZero(ls):
    i=0
    naturals=[]
    while i<len(ls):
        if ls[i]>0:
            naturals.append(ls[i])
        i=i+1          
    return naturals

ls=[0, -3, 7, 2, -5, 1]
positiva=aboveZero(ls)
print(positiva)
