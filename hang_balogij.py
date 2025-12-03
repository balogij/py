def Hangtartomany(frekvencia):
    global vege
    if frekvencia < 0:
        return "Érvénytelen frekvencia"
    elif frekvencia == 0:
        vege = True
        return "Vége"
    elif frekvencia < 20:
        return "A(z) infra tartományba tartozik."
    elif 20 <= frekvencia <= 20000:
        return "A(z) hallható tartományba tartozik."
    elif frekvencia > 20000:
        return "A(z) ultra tartományba tartozik."
    
#main
vege = False
while not vege:
    egesz = False
    while not egesz:
        try:
            frekvencia = int(input("Kérem, adjon meg egy frekvenciát (Hz): "))
            if frekvencia < 0:
                print("A frekvencia nem lehet negatív szám!")
                egesz = False
            else:
                egesz = True
        except ValueError:
            print("Érvénytelen bemenet! Kérem, számot adjon meg.")
            egesz = False

    if egesz:
        eredmeny = Hangtartomany(frekvencia)        
        print(eredmeny)
