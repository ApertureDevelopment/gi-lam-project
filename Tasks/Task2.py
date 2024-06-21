def größteZahl(liste):
    xMax = liste[0]
    for zahl in liste:
        if zahl > xMax:
            xMax = zahl
    return xMax
