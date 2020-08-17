"""
oszthatóság
    páros szám kitalálása eg.:(x % 2)

binary search tree
- open phone book in the middle
-- check if name is on the pages
- if its before
-- open to half of the remaining pages
- goto line 7
- if its NOT before
- goto line 9
- repeat until name is found
"""





nev = input("Név: ")
szuletesi_ev = int(input("Születési év: "))
eletkor = 2020 - szuletesi_ev

def felnott (szuletesi_ev: int):
    if eletkor >= 18:
        return True
    else:
        return False


def parosSzam(szam: int):
    if szam % 2 == 0:
        return True
    else:
        return False


if felnott(eletkor):
    print(nev + " idosebb mint 18")
    if parosSzam(szuletesi_ev):
        print(nev, "eletkora paros")
    else:
        print(nev, "eletkora paratlan")
else:
    print(nev + " fiatalabb mint 18")
