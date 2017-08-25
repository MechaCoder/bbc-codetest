def romannumeralgenerator(rootint: int):
    """ converts a entered interger into a string of roman numerals """

    rsting = [] #type: list
    while rootint > 0:
        if rootint >= 1000:
            rootint -= 1000
            rsting.append('M')
            continue

        if rootint >= 900:
            rootint -= 900
            rsting.append('CM')
            continue

        if rootint >= 500:
            rootint -= 500
            rsting.append('D')
            continue

        if rootint >= 400:
            rootint -= 400
            rsting.append('CD')
            continue

        if rootint >= 100:
            rootint -= 100
            rsting.append('C')
            continue

        if rootint >= 90:
            rootint -= 90
            rsting.append('XC')
            continue
            
        if rootint >= 50:
            rootint -= 50
            rsting.append('L')
            continue

        if rootint >= 40:
            rootint -= 40
            rsting.append('XL')
            continue

        if rootint >= 10:
            rootint -= 10
            rsting.append('X')
            continue

        if rootint >= 9:
            rootint -= 9
            rsting.append('IX')
            continue

        if rootint >= 5:
            rootint -= 5
            rsting.append('V')
            continue

        if rootint >= 4:
            rootint -= 4
            rsting.append('IV')
            continue

        if rootint >= 1:
            rootint -= 1
            rsting.append('I')
            continue

    return ''.join(rsting)
