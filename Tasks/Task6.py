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


# Alternative approach
def swap(array, iterA, iterB):
    temp = array[iterA]
    array[iterA] = array[iterB]
    array[iterB] = temp

def altSort(array):
    iter = 0
    array_length = len(array)

    while iter < array_length:
        if i + 1 == array_length: return;
        if array[i] > array[i + 1]:
            swap(array, i, i + 1)
            if(i > 0):
                i = i - 1
        else:
            i = i + 1