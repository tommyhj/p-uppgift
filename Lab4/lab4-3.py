import math

def standardavvikelse(datapunkter):
    # Räknar ut standardavvikelsen av punkterna i listan data
    summa = 0
    for i in range(len(datapunkter)):
        summa += math.pow((datapunkter[i] - (sum(datapunkter) / len(datapunkter))), 2)
    return math.sqrt( (1/(len(datapunkter)-1) )*summa)

datapunkter = [1, 2, 3, 7, 9]
print(standardavvikelse(datapunkter))


