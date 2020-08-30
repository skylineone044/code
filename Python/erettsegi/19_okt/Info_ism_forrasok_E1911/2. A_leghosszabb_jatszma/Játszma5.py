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
   pass 