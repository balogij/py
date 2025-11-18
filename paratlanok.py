def paratlan(szam):
    if(szam%2==0):
        return False
    else:
        return True

def bevitel():
    global szamok

    egesz = True
    while(egesz):
        try:
            szam = int(input("adj meg egy egész számot: "))
            szamok.append(szam)
            egesz = False
        except:
            print("nem egész szám")

def legkissebb(szamok):
    global db_szam
    kissebb = szamok[0]
    for i in range(db_szam):
        if(kissebb>szamok[i]):
            kissebb = szamok[i]
    return kissebb

def legnagyobb(szamok):
    global db_szam
    nagyobb = szamok[0]
    for i in range(db_szam):
        if(nagyobb<szamok[i]):
            nagyobb = szamok[i]
    return nagyobb

def kicsi_nagy(szamok):
    kicsinagy = []
    global db_szam
    kissebb = szamok[0]
    nagyobb = szamok[0]
    for i in range(db_szam):
        if(nagyobb<szamok[i]):
            nagyobb = szamok[i]
        if(kissebb>szamok[i]):
            kissebb = szamok[i]
    kicsinagy = [kissebb,nagyobb]
    return kicsinagy


#main
szamok = []
szamok.clear()

egesz = True
while(egesz):
    try:
        db_szam = int(input("Hány számot akarsz megadni: "))
        egesz = False
    except:
        print("nem egész szám")


for i in range(db_szam):
    bevitel()

print(szamok)

#for i in range(db_szam):
#    if(paratlan(szamok[i])==True):
#        db_paratlan = db_paratlan +1
kicsinagy = []
kicsinagy = kicsi_nagy(szamok)
kissebb = kicsinagy[0]
nagyobb = kicsinagy[1]
print(f"A legkissebb ({kissebb}) és a legnagyobb ({nagyobb}) különbsége {nagyobb-kissebb}.")