import math


def array_median(array):
    tempArray = array.copy()
    tempArray.sort()

    middle = len(array) / 2
    if tempArray % 2 != 0:
        middle = math.ceil(middle)
        return tempArray[middle]
    else:
        return (tempArray[middle] + tempArray[middle + 1]) / 2