# die vorgegebene Zahlenfolge:
zahlen = [4, 23, 8, 13, 7, 9, 42, 11, 6, 80, 3]


# Sortierfunktion
def minisort(sortZahlen):
    doSort = True

    while doSort:
        doSort = False
        i = 0
        for i in range(len(sortZahlen)-1):


            zahlA = sortZahlen[i]
            zahlB = sortZahlen[i+1]
            if zahlA>zahlB:
                    doSort = True
                    sortZahlen[i+1]=zahlA
                    sortZahlen[i]=zahlB
    return sortZahlen



print(zahlen)
zahlen = minisort(zahlen)
print ('Sortierte Zahlenfolge:')
print(zahlen)











#sort(zahlen)
