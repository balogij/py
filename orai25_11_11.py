def colored(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

feladat_leiras = ["Írj programot ami beolvassa a felhasználó nevét, majd köszön neki, a nevén szólítva őt!","Állítsa elő a következő alakzatot! /n********** /noooooooooo","Állítsa elő a következő alakzatot! /n*o*o*o*o*o /n*o*o*o*o*o","Kérjen be két egész számot a felhasználótól, és írja ki a két szám összegét!","Kérjen be három egész számot a felhasználótól, és írja ki a három szám összegét!","for","Kérj be egy egész számot, addig amíg nem nulla a megadott szám","Print 'end' paraméter","írj programot, mely kiírja a primszámokat 1-től 100-ig!"]

feladatok_szama = len(feladat_leiras)
ervenyes = False
while not ervenyes:
    try:
        feladat_sorszam = int(input("Add meg a feladat sorszámát (1-"+ str(feladatok_szama) +"):"))-1
        if feladat_sorszam>=0 and feladat_sorszam<feladatok_szama:
            ervenyes = True
        else:
            print("1-"+ str(feladatok_szama) + " közötti számot adjál meg")
    except ValueError:
        print("Ez nem egész szám!")

leiras_szettort = feladat_leiras[feladat_sorszam].split("/n")
print("Feladat leírás:")

match feladat_sorszam:
    case 0:
        for sub_str in leiras_szettort:
            print(colored(255,0,0,sub_str))

        print("megoldas:")
        print("")
        user_name = str(input("Kérlek add meg a neved:"))
        print("Helló " + user_name +" üdvözöllek!")
    case 1:
        for sub_str in leiras_szettort:
            print(colored(255,0,0,sub_str))

        print("megoldas:")
        print("")
        szoveg = ["**********","oooooooooo"]
        print(szoveg[0])
        print(szoveg[1])
    case 2:
        for sub_str in leiras_szettort:
            print(colored(255,0,0,sub_str))

        print("megoldas:")
        print("")
        szoveg1 = str("")
        csillag = str("*")
        kor = str("o")
        for i in range(5):
            szoveg1 = szoveg1 + csillag
            szoveg1 = szoveg1 + kor
        print(szoveg1)
        print(szoveg1)
    case 3:
        for sub_str in leiras_szettort:
            print(colored(255,0,0,sub_str))

        ervenyes = False
        while not ervenyes:
            try:
                elso_szam = int(input("Add meg az első egész számot:"))
                ervenyes = True
            except ValueError:
                print("Ez nem egész szám!")
        ervenyes = False
        while not ervenyes:
            try:
                masodik_szam = int(input("Add meg a másidik egész számot:"))
                ervenyes = True
            except ValueError:
                print("Ez nem egész szám!")
        print(str(elso_szam) + "+" + str(masodik_szam) + "=" + str(elso_szam+masodik_szam))
    case 4:
        for sub_str in leiras_szettort:
            print(colored(255,0,0,sub_str))

        ervenyes = False
        while not ervenyes:
            try:
                elso_szam = int(input("Add meg az első egész számot:"))
                ervenyes = True
            except ValueError:
                print("Ez nem egész szám!")
        ervenyes = False
        while not ervenyes:
            try:
                masodik_szam = int(input("Add meg a másidik egész számot:"))
                ervenyes = True
            except ValueError:
                print("Ez nem egész szám!")
        ervenyes = False
        while not ervenyes:
            try:
                harmadik_szam = int(input("Add meg a harmadik egész számot:"))
                ervenyes = True
            except ValueError:
                print("Ez nem egész szám!")
        print(str(elso_szam) + "+" + str(masodik_szam) + "+" + str(harmadik_szam) + "=" + str(elso_szam+masodik_szam+ harmadik_szam))
    case 5:
        for sub_str in leiras_szettort:
            print(colored(255,0,0,sub_str))

        for i in range(5):
            if i == 3:
                i=11
                print(i)
                continue
            print(i)
        
        szamlalo = int(1)
        for i in ("Helló világ"):
            if i!=" ":
                match szamlalo:
                    case 1:
                        print(colored(255,0,0,i))
                    case 2:
                        print(colored(0,255,0,i))
                    case 3:
                        print(colored(0,0,255,i))
                    case 4:
                        print(colored(255,255,0,i))
                szamlalo = szamlalo + 1
            else:
                print(i)
            if szamlalo>4:
                szamlalo = 1
    case 6:
        for sub_str in leiras_szettort:
            print(colored(255,0,0,sub_str))

        szam = int(-1)
        while(szam!=0):
            ervenyes = False
            while not ervenyes:
                try:
                    szam = int(input("Adj meg egy egész számot:"))
                    print(szam)
                    ervenyes = True
                except:
                    print("Ez nem egész szám!")
    case 7:
        for sub_str in leiras_szettort:
            print(colored(255,0,0,sub_str))

        szoveg ="Helló világ"
        for betu in szoveg:
            print(betu,end="*")

        print("")
        hossz = int(len(szoveg))
        print(str(hossz))            
        for betu in range(hossz,0,-1):
            print(szoveg[betu-1])                        
    case 8:
        for sub_str in leiras_szettort:
            print(colored(255,0,0,sub_str))
        
        max = int(101)

        szam = int(3)
        oszto = int(2)

        while szam<101:
            prim = False
            while oszto<=szam and prim==False:
                if oszto==szam:
                    print(str(szam))
                    prim = True
                elif (szam%oszto)==0:
                    prim = True
                #print(str(szam)+"/"+str(oszto))
                oszto = oszto +1
            szam = szam + 1
            oszto = 2
            prim = False