def kleinsteZahl(liste):
    xMin = liste[0]
    for zahl in liste:
        if zahl < xMin:
            xMin = zahl
    return xMin
