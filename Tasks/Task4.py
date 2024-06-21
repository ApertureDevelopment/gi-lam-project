def durchschnitt(liste):
    summe = 0.0
    zähler = 0
    for zahl in liste:
        summe = summe + zahl
        zähler = zähler + 1
    return summe / zähler
