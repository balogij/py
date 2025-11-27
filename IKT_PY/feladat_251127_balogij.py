feladatok = ['1. Kérj be két számot, és írd ki az összegüket.',
'2. Kérj be egy számot, és döntsd el, hogy páros-e.',
'3. Kérj be három számot, és írd ki melyik a legnagyobb.',
'4. Kérj be egy N értéket, majd írd ki 1-től N-ig a számokat egy ciklussal.',
'5. Kérj be egy N számot, majd számold ki a közötti számok összegét.',
'6. Kérj be 5 darab számot, tedd őket listába, majd számold ki az átlagukat.',
'7. Adj meg egy listát tetszőleges egész számokkal, majd írd ki: a legnagyobb értéket és a legkisebb értéket',
'8. Kérj be egy számot és döntsd el, hogy benne van-e az előre adott listában.',
'9. Adott egy lista számokkal. Készíts új listát, amelyben csak a páros számok szerepelnek.',
'10. Írj programot, ami egy listát buborékrendezéssel növekvő sorrendbe tesz.']

countFeladat = len(feladatok)

#main
fut = True
while (fut):
    nemszam = True
    while(nemszam):
        bevitel = input(f'Melyik feladatot választod (1-{countFeladat} vagy "K" kilépés) : ')
        try:
            sorszam = int(bevitel)
            nemszam = False
        except ValueError:
            if(bevitel == 'k'):
                nemszam = False
                fut = False
                print('Viszlát!')
            else:
                print('Ez nem szám!')
    if fut:
        sorszam = int(bevitel)
        print(sorszam)
        match(sorszam):
            #első feladat
            case 1:
                print(feladatok[sorszam-1])
                print('Megoldas:')
                notnumber = True
                while(notnumber):
                    try:
                        elso = float(input('Kérem az első számot: '))
                        notnumber = False
                    except ValueError:
                        print('Ez nem szám!')
                notnumber = True
                while(notnumber):
                    try:
                        masodik = float(input('Kérem a második számot: '))
                        notnumber = False
                    except ValueError:
                        print('Ez nem szám!')
                print(f'Az első és a második szám összege: {elso}+{masodik}={elso+masodik}')
            #második feladat
            case 2:
                print(feladatok[sorszam-1])
                print('Megoldas:')
                notnumber = True
                while(notnumber):
                    try:
                        elso = int(input('Kérek egy egész számot: '))
                        notnumber = False
                    except ValueError:
                        print('Ez nem szám!')
                if(elso>0 or elso<0):
                    if(elso%2 == 0):
                        print(f'A(z) {elso} páros szám')
                    else:
                        print(f'A(z) {elso} páratlan szám')
                else:
                    print('a megadott szám a nulla')
            #3. feladat
            case 3:
                print(feladatok[sorszam-1])
                print('Megoldas:')
                szamok = []
                legnagyobb = 0
                for _ in range(3):
                    notnumber = True
                    while(notnumber):
                        try:
                            elso = float(input('Kérek egy számot: '))
                            szamok.append(elso)
                            notnumber = False
                        except ValueError:
                            print('Ez nem szám!')
                    if(elso>legnagyobb and len(szamok)>1):
                        legnagyobb = elso
                    elif len(szamok)==1:
                        legnagyobb = elso
                    print(legnagyobb)
                print(f'A három szám közül ({szamok}) a(z) {legnagyobb} a legnagyobb szám.')
            #4. feladat    
            case 4:
                print(feladatok[sorszam-1])
                print('Megoldas:')
                notnumber = True
                while(notnumber):
                    try:
                        szam = int(input('Kérek egy számot: '))
                        notnumber = False
                    except ValueError:
                        print('Ez nem szám!')
                
                if(szam>0):
                    for i in range(1,szam+1):
                        print(i)
                else:
                    for i in range(1,szam-1,-1):
                        print(i)
            #5. feladat
            case 5:
                print(feladatok[sorszam-1])
                print('Megoldas:')
                notnumber = True
                while(notnumber):
                    try:
                        darab = int(input('Hány darab számot kérjünk be?: '))
                        notnumber = False
                    except ValueError:
                        print('Ez nem szám!')
                szamok = []
                for i in range(darab):
                    notnumber = True
                    while(notnumber):
                        try:
                            elso = int(input('Kérek egy számot: '))
                            szamok.append(elso)
                            notnumber = False
                        except ValueError:
                            print('Ez nem szám!')
                for i in range(darab-1):
                    osszeg = 0
                    for x in range(szamok[i]+1,szamok[i+1]):
                        osszeg += x
                    print(f'A(z) {szamok[i]} és {szamok[i+1]} közti számok összege: {osszeg}')
            #6. feladat
            case 6:
                print(feladatok[sorszam-1])
                print('Megoldas:')
                szamok = []
                osszeg = 0
                for i in range(5):
                    notnumber = True
                    while(notnumber):
                        try:
                            elso = int(input('Kérek egy egész számot: '))
                            szamok.append(elso)
                            osszeg += elso
                            notnumber = False
                        except ValueError:
                            print('Ez nem szám!')
                print(f'A {szamok} átlaga {osszeg/5}.')
            #7. feladat
            case 7:
                print(feladatok[sorszam-1])
                print('Megoldas:')
                szamok =[2,4,12,3,6,7,9,8,11]
                print(f'A {szamok} között')
                print(f'A legnagyobb a(z) {max(szamok)}')
                print(f'A legkissebb a(z) {min(szamok)}')
            #8. feladat
            case 8:
                print(feladatok[sorszam-1])
                print('Megoldas:')
                szamok =[2,4,12,3,6,7,9,8,11]
                notnumber = True
                while(notnumber):
                    try:
                        elso = int(input('Kérek egy egész számot: '))
                        notnumber = False
                    except ValueError:
                        print('Ez nem szám!')
                if elso in szamok:
                    print(f'A(z) {elso} szerepel a {szamok} között')
                else:
                    print(f'A(z) {elso} nem szerepel a {szamok} között')
            #9. feladat
            case 9:
                print(feladatok[sorszam-1])
                print('Megoldas:')
                szamok =[2,4,12,3,6,7,9,8,11]
                parosak = []
                for szam in szamok:
                    if(szam%2==0):
                        parosak.append(szam)
                print(f'A {szamok} közül az {parosak} a páros számok')
            #10. feladat
            case 10:
                print(feladatok[sorszam-1])
                print('Megoldas:')
