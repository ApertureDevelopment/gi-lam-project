from decimal import *


def array_avg(liste):
    sum = 0
    counter = 0
    for number in liste:
        sum = sum + number
        counter = counter + 1
    return Decimal(sum) / Decimal(counter)
