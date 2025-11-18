import math

def pi():
    piii = math.pi
    return piii

def oszeadas(szam_1,szam_2):
    oszeg = szam_1+szam_2
    return oszeg

def kerulet(sugar):
    r_kerulet = 2 * sugar * pi()
    return r_kerulet

#main

rossz_ertek = True
while(rossz_ertek):
    try:
        szam_1 = float(input("Add meg az első számot: "))
        rossz_ertek = False
    except:
        print("ez nem valós szám")
rossz_ertek = True
while(rossz_ertek):
    try:
        szam_2 = float(input("Add meg a második: "))
        rossz_ertek = False
    except:
        print("ez nem valós szám")

print(str(szam_1) +"+"+str(szam_2)+"="+str(oszeadas(szam_1,szam_2)))

rossz_ertek = True
while(rossz_ertek):
    try:
        szam_1 = float(input("Add meg a kör sugarát: "))
        rossz_ertek = False
    except:
        print("ez nem valós szám")
print(f"A kör kerülete: {kerulet(szam_1)}")