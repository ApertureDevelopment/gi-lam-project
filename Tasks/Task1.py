def smallest_number(liste):
    array_min = liste[0]
    for number in liste:
        if number < array_min:
            array_min = number
    return array_min
