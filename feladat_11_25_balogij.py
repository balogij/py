szamok = [-14, 23, 1, -48, -43, 28, -77, -33, -95, 38, -9, 98, -61, 58, 21, 87, 41, -65, -22, -20, -56, -75, 80, -77, 100]

def kissebbek(lista,max):
    darab = 0
    for szam in lista:
        if(szam<max):
            darab += 1
    return darab

#main
print('1. feladat')
egesz = True
while(egesz):
    try:
        szam_max = int(input("Adjon meg egy egész számot:"))
        print(f"A listában {kissebbek(szamok,szam_max)}db kisebb szám szerepel")
        egesz = False    
    except:
        print('Ez nem egész szám!')

print('2. feladat')

print('3. feladat')

print('4. feladat')

print('5. feladat')

