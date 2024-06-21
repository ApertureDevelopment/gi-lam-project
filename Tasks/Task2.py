def biggest_number(liste):
    array_max = liste[0]
    for number in liste:
        if number > array_max:
            array_max = number
    return array_max
