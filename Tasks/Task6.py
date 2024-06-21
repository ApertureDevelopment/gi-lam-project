# die vorgegebene Zahlenfolge:
zahlen = [4, 23, 8, 13, 7, 9, 42, 11, 6, 80, 3]


# Sortierfunktion
def minisort(sortZahlen):
    counter = 1 #irgendein wert über 0

    while counter >0:
        counter = 0
        i = 0
        for i in range(len(sortZahlen)-1):


            zahlA = sortZahlen[i];
            zahlB = sortZahlen[i+1];
            if zahlA>zahlB:
                    counter = counter + 1
                    sortZahlen[i+1]=zahlA
                    sortZahlen[i]=zahlB
    print('Rückgabe:')
    return sortZahlen


print(zahlen)
zahlen = minisort(zahlen)
print(zahlen)











#sort(zahlen)
