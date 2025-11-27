feladatok = ['Kérj be két számot, és írd ki az összegüket.',
'Kérj be egy számot, és döntsd el, hogy páros-e.',
'Kérj be három számot, és írd ki melyik a legnagyobb.',
'Kérj be egy N értéket, majd írd ki 1-től N-ig a számokat egy ciklussal.',
'Kérj be egy N számot, majd számold ki a közötti számok összegét.',
'Kérj be 5 darab számot, tedd őket listába, majd számold ki az átlagukat.',
'Adj meg egy listát tetszőleges egész számokkal, majd írd ki: a legnagyobb értéket és a legkisebb értéket'
'Kérj be egy számot és döntsd el, hogy benne van-e az előre adott listában.']

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
                
                if(szam>=0):
                    for i in range(1,szam):
                        print(i)
                else:
                    for i in range(szam,1):
                        print(i)
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
                for i in range(darab):
                    notnumber = True
                    while(notnumber):
                        try:
                            elso = float(input('Kérek egy számot: '))
                            szamok.append(elso)
                            notnumber = False
                        except ValueError:
                            print('Ez nem szám!')
            case 6:
                print(feladatok[sorszam-1])
                print('Megoldas:')
