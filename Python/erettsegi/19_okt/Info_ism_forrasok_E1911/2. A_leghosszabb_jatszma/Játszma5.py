def feladat3():
    with open("labdamenetek5.txt") as f:
        raw_labdamenetek = f.read()
    n = 0
    # print(raw_labdamenetek)
    labdamenetek = []
    while n < len(raw_labdamenetek):
        if not raw_labdamenetek[n] == "\n":
            labdamenetek.append(raw_labdamenetek[n])
        n += 1
    return labdamenetek


print("Feladat 3: ", len(feladat3()))

labdamenetek = feladat3()

def feladat4():
    i = 0
    adogato_nyert_szama = 0
    fogado_nyert_szama = 0
    while i < len(labdamenetek):
        if labdamenetek[i] == "A":
            adogato_nyert_szama += 1
        else:
            fogado_nyert_szama += 1
        i += 1
    adogato_nyeresi_szazalek = adogato_nyert_szama / len(labdamenetek) * 100
    return adogato_nyeresi_szazalek

print("Feladat 4: adogato ", str(feladat4()) + "%-ban nyerte meg a labdameneteket")

def feladat5():
    n = 0
    adogato = 0
    fogado = 0
    fogado_win = 0
    adogato_win = 0
    while n < len(labdamenetek):
        element = labdamenetek[n]
        if element == "A":
            adogato += 1
        else:
            fogado += 1
        if fogado == 4:
            fogado_win += 1
            hanyadik_jatek = fogado_win + adogato_win
            print(str(hanyadik_jatek) + ". jatek | gyozets: fogado (" + str(fogado) + ":" + str(adogato) + ")" )
            fogado = 0
            adogato = 0
        elif adogato == 4:
            adogato_win += 1
            hanyadik_jatek = fogado_win + adogato_win
            print(str(hanyadik_jatek) + ". jatek | gyozets: adogato (" + str(fogado) + ":" + str(adogato) + ")" )
            adogato = 0
            fogado = 0
        else:
            pass
        n += 1
    print("adogato gyozelem: " + str(adogato_win))
    print("fogado gyozelem: " + str(fogado_win))
    return 0

feladat5() # nem a kert feladat e nem is jo xdd

class Játék:
    def __init__(self, állás, adogatoNev, fogadoNev, ):
        pass