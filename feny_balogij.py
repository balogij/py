#vörös: 620 - 780 nm
#narancs: 585 - 620 nm 
#sárga: 570 - 585 nm
#zöld: 490 - 570 nm
#kék: 440 - 490 nm
#indigókék: 420 - 440 nm

#main
egesz = False
while not egesz:
    try:
        hullamhosz = int(input("Kérem, adjon meg egy hullámhosszt (nm): "))
        if hullamhosz < 0:
            print("A hullámhossz nem lehet negatív szám!")
            egesz = False
        else:
            egesz = True
    except ValueError:
        print("Érvénytelen bemenet! Kérem, számot adjon meg.")
        egesz = False

if egesz:
    match hullamhosz:
        case _ if 620 <= hullamhosz <= 780:
            print("Vörös színnek látjuk")
        case _ if 585 <= hullamhosz < 620:
            print("Narancs színnek látjuk")
        case _ if 570 <= hullamhosz < 585:
            print("Sárga színnek látjuk")
        case _ if 490 <= hullamhosz < 570:
            print("Zöld színnek látjuk")
        case _ if 440 <= hullamhosz < 490:
            print("Kék színnek látjuk")
        case _ if 420 <= hullamhosz < 440:
            print("Indigókék színnek látjuk")
        case _:
            print("Nem látható.")   
