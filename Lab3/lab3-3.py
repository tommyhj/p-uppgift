def is_prime(tal):
    # Funktionen returnerar True respektive False beroende på om "tal" är ett primtal
    primlist = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
    new_prime = [101]

    if tal == 2:
        return True
    # Sortera ut tal som är delbara med 2 eller lika med 1
    if tal % 2 == 0 or tal == 1:
        return False
    # Sortera ut tal vi redan vet är primtal
    if tal in primlist or tal in new_prime:
        return True

    # Loopa från det största värdet i new_prime till värdet tal för att få med alla primtal därimellan, skippa jämna tal
    for i in range(new_prime[-1], tal+2, 2):

        # Loopa antalet tal som finns i primlist och new_prime
        for j in range(0, len(primlist) + len(new_prime)+1):

            # Så länge antalet varv är mindre än längden på primlist, utvärdera om talet är delbart med något i primlist
            if j < len(primlist):
                if tal % primlist[j] == 0:
                    return False
            # Så länge antalet varv i < längden på primlist+new_prime, utvärdera om delbart med något i listorna
            elif j <= len(primlist) + len(new_prime):
                if tal % new_prime[j - len(primlist)-1] == 0:
                    return False
            else:
                new_prime.append(j)
        return True

tal1 = int(input("Från vilket tal: "))
tal2 = int(input("Till vilket tal: "))
print("Primtalen från", tal1, "till", tal2, "är:")
for n in range(tal1, tal2):
    if is_prime(n):
        print(n)
