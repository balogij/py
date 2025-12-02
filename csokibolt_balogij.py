from csoki_balogij import Csoki

def AtlagSuly(lista, csoki_tipus):
    ossz_suly = 0
    for csoki in lista:
        if csoki.tipus == csoki_tipus:
            ossz_suly += csoki.tomeg
    atlag = ossz_suly / len(lista)
    return atlag

def CsomagolasSum(lista, csomagolas_tipus):
    ossz_csomagolas = 0
    for csoki in lista:
        if csoki.csomagolas == csomagolas_tipus:
            ossz_csomagolas += 1
    return ossz_csomagolas

def AdatBetoltes(fajlnev):
    csoki_lista = []
    try:
        file = open(fajlnev, "r", encoding="utf-8")
        adatok = file.read()
        sorok = adatok.split("\n")
        for sor in sorok:
            adatok = sor.split(";")
            if len(adatok) == 3:
                tipus = adatok[0]
                tomeg = int(adatok[1])
                csomagolas = adatok[2]
                csoki = Csoki(tipus, tomeg, csomagolas)
                csoki_lista.append(csoki)
        return csoki_lista
    except FileNotFoundError:
        print(f"Hiba: A '{fajlnev}' fájl nem található.")
        return []
    except IOError as e:
        print(f"Hiba történt a fájl olvasásakor: {e}")
        return []
    
def Keres(keresett):
    global csokik
    for csoki in csokik:
        if (keresett.tipus == csoki.tipus and keresett.tomeg == csoki.tomeg and keresett.csomagolas == csoki.csomagolas):
            return csoki.Ar()
    return -1

def Adatbekeres():
    global csokik
    rossz_bemenet = False
    while not rossz_bemenet:
        try:
            tipus = input("Kérem, adja meg a csoki típusát (ét, tej, fehér): ")
            if tipus not in ["ét", "tej", "fehér"]:
                print("Kérem, megfelelő értéket adjon meg (ét, tej, fehér).")
            else:
                rossz_bemenet = True
        except ValueError:
            print("Érvénytelen bemenet! Kérem, szöveget adjon meg (ét, tej, fehér).")
    rossz_bemenet = False
    while not rossz_bemenet:
        try:
            tomeg = int(input("Kérem, adja meg a csoki tömegét (g): "))
            if tomeg <= 0:
                print("A tömegnek pozitív egész számnak kell lennie!")
            else:
                rossz_bemenet = True
        except ValueError:
            print("Kérem, számot adjon meg.")
    rossz_bemenet = False
    while not rossz_bemenet:
        try:
            csomagolas = input("Kérem, adja meg a csoki csomagolását (papír/doboz/kimérős): ")
            if csomagolas not in ["papír", "doboz", "kimérős"]:
                print("Kérem, megfelelő értéket adjon meg (papír/doboz/kimérős).")
            else:
                rossz_bemenet = True
        except ValueError:
            print("Kérem, megfelelő értéket adjon meg (papír/doboz/kimérős).")
    rossz_bemenet = False
    while not rossz_bemenet:
        try:
            darabszam = int(input("Kérem, adja meg hány adagot szeretne: "))
            if darabszam <= 0:
                print("Az darabszámnak pozitív egész számnak kell lennie!")
            else:
                rossz_bemenet = True
        except ValueError:
            print("Kérem, egész számot adjon meg.")
    uj_csoki = Csoki(tipus, tomeg, csomagolas)
    keresett_ar = Keres(uj_csoki)
    if keresett_ar == -1:
        valasz = "Hiánycikk"
    else:
        valasz = f"A termék ({tipus}, {tomeg}g, {csomagolas} csomagolás, {darabszam} adag) ára: {keresett_ar*darabszam} Ft"
    return valasz

#main
csokik = AdatBetoltes("csokibolt.txt")
if csokik:
    print(f"A fehér csokik átlagos tömege: {AtlagSuly(csokik, 'fehér')}g")
    print(f"Összesen {CsomagolasSum(csokik, 'papír')} papír csomagolású csoki van.")

print(Adatbekeres())
