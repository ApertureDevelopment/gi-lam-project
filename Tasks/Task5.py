def median(liste):
    liste.sort()
    zähler = 0
    for zahl in liste:
        zähler = zähler + 1
    index = zähler / 2
    return liste[int(index)]
