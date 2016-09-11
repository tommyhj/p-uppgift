def medel(listdata):
    # Räknar ut medelvärdet av en listas värden
    return sum(listdata)/len(listdata)

numerus = int(input("Hur många år vill du mata in? "))
ls = [""]*12*numerus
anno = [""]*numerus

# Denna loop samlar in informationen om antalet år och tempen per månad
i = 0
while i < numerus:
    if i < 3:
        print("Vilket år är {}:a året?".format(i+1), end="")
    else:
        print("Vilket år är {}:e året?".format(i+1), end="")
    anno[i] = int(input())
    for j in range(1, 13):
        print("Månad {}:".format(j), end="")
        ls[i*12+j-1] = int(input())
    i+=1

print("Sammanställning:")
# Denna loop skriver ut en sammanställning av temperaturerna
for k in range(numerus):
    print("År {}:".format(anno[k]))
    a_list = [""]*12
    for l in range(12):
        for m in range(12):
            a_list[m] = ls[k*12+m]
        print("Månad {}: {}".format(l+1, ls[k*12+l]), end=" ")
        if ls[k*12+l] == max(a_list):
            print("HTÅ ", end="")
            if ls[k*12+l] == max(ls):
                print("ATH")
            else:
                print("")
        else:
            print("")
    print("Genomsnittlig temperatur för år {}: {}".format(anno[k], medel(a_list)))