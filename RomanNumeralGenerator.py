
class RomanNumeralGenerator:

    def __init__(self) -> None:
        pass

    def convertNumber(self, rootInt: int) -> str:
        """ converts numbers from base to roman"""

        rsting = []
        while rootInt > 1:
            if rootInt > 1000:
                rootInt -= 1000
                rsting.append('M')
                continue

            if rootInt > 900:
                rootInt -= 900
                rsting.append('CM')
                continue

            if rootInt > 500:
                rootInt -= 500
                rsting.append('D')
                continue

            if rootInt > 400:
                rootInt -= 400
                rsting.append('CD')
                continue

            if rootInt > 100:
                rootInt -= 100
                rsting.append('C')
                continue

            if rootInt > 90:
                rootInt -= 90
                rsting.append('XC')
                continue
            
            if rootInt > 50:
                rootInt -= 50
                rsting.append('L')
                continue

            if rootInt > 40:
                rootInt -= 40
                rsting.append('XL')
                continue

            if rootInt > 10:
                rootInt -= 10
                rsting.append('X')
                continue

            if rootInt > 9:
                rootInt -= 9
                rsting.append('IX')
                continue

            if rootInt > 5:
                rootInt -= 5
                rsting.append('V')
                continue

            if rootInt > 4:
                rootInt -= 4
                rsting.append('IV')
                continue

            if rootInt > 1:
                rootInt -= 1
                rsting.append('I')
                continue


        return ''.join(rsting)