

def kleinsteZahl(liste):
    y = liste[0]
    for x in liste:
        if x < y:
            y = x
    return y


def größteZahl(liste):
    y = liste[0]
    for x in liste:
        if x > y:
            y = x
    return y


def summe(liste):
    sum = 0
    for x in liste:
        sum = sum + x
    return sum

def durchschnitt(liste):
    sum = 0.0
    zähler = 0
    for x in liste:
        sum = sum + x
        zähler = zähler + 1
    return sum / zähler

def median(liste):
    liste.sort()
    zähler = 0
    for x in liste:
        zähler = zähler + 1
    index = zähler / 2
    return liste[int(index)]


print(kleinsteZahl([-3, -1, 0, 15, 6]))
print(größteZahl([-3, -1, 0, 15, 6]))
print(summe([-3, -1, 0, 15, 6]))
print(durchschnitt([-3, -1, 0, 15, 6]))
print(median([-3, -1, 9, 15, 6]))