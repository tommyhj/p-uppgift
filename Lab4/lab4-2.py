def medel(ls):
    # Returnerar medelvärdet av en lista utan att använda len eller sum
    summa, j = 0, 0
    for i in ls:
        summa += ls[j]
        j += 1
    return summa / (j)

lista = [1,4, 5, 6, 7, 55, 5]
print(medel(lista))
