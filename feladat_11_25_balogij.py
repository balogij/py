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

sz_ind = len(szamok)-1
oszthato_7tel = False

while(oszthato_7tel== False and sz_ind>0):
    if(szamok[sz_ind]%7==0):
        print(f"Az utolsó 7-tel osztható szám a listában a {sz_ind+1}. elem")
        oszthato_7tel = True
    sz_ind -= 1

print('3. feladat')
print(f"{len(szamok)} szám szerepel a listában")

print('4. feladat')

sz_ind = len(szamok)-1
oszthato_15tel = []

print("A lista 15-tel osztható számainak a fele:")
kiirando = ""
for szam in szamok:
    if(szam%15==0):
        kiirando += str(szam) +"/2=" + str(szam/2)+"   "
        oszthato_15tel.append(szam)
oszthato_db = len(oszthato_15tel)
if(oszthato_db>0):
    print(f"A listában {oszthato_db} darab 15-tel osztható szám szerepel ennek a fele {oszthato_db/2}.")
    print(kiirando)

print('5. feladat')
utolsoelotti = len(szamok)-2
kovetnegativotpozitiv = False
knp_lista = []
for i in range(utolsoelotti):
    if(szamok[i]<0 and szamok[i+1]>0):
        kovetnegativotpozitiv = True
        knp_lista.append(szamok[i])
if(kovetnegativotpozitiv):
    print("A listában van olyan negatív szám amit pozitív követ")
    print(f"Ez(ek) a {knp_lista} szám(ok)")
else:
    print("A listában nincs olyan negatív szám, amit pozitív követ")

