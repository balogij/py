import random

class Csoki:
    def __init__(self, fajta="", kiszereles=0, csomag="") -> None:
        self.tipus = fajta
        self.tomeg = kiszereles
        self.csomagolas = csomag

    def Ar(self):
        match self.csomagolas:
            case 'kimérős':
                return self.tomeg*3
            case 'papír':
                return self.tomeg*3+100
            case 'doboz':
                return self.tomeg*3+500

csoki_t = ['ét','tej','fehér','ét','tej','fehér','ét','tej','fehér']
csoki_kisz = ['kimérős','papír','doboz','kimérős','papír','doboz','kimérős','papír','doboz']

csokik = []
for _ in range(10):
    csokik.append(Csoki(csoki_t[random.randrange(0,9)], int(random.randrange(100,500,25)),csoki_kisz[random.randrange(0,9)]))

szoveg = ''
for cur in csokik:
    print(f'{cur.tipus} , {cur.tomeg}, {cur.csomagolas}')
    szoveg += cur.tipus +';'+ str(cur.tomeg) +';'+ cur.csomagolas +'\n'

target_file = open("csokibutik.txt", "w", encoding='utf-8', newline='\n')
print(f"{szoveg}", file=target_file)

file_name = "C:\\users\\balogij\\desktop\\py\\csokibutik.txt"
target_file.close()

try:
    with open(file_name, 'r', encoding='utf-8') as file:
        file_contents = file.read()
        target_file.close()
    
    print("A fájl teljes tartalma:\n")
    print(file_contents)

except FileNotFoundError:
    print(f"Hiba: A '{file_name}' nevű fájl nem található.")
except Exception as e:
    print(f"Hiba történt a fájl beolvasása közben: {e}")

if(len(file_contents)>0):
    csokik = []
    szavak = file_contents.split(';')
    ind = 0
    count = len(szavak)-1
    while(ind<count):
        egy_csoki = Csoki()
        egy_csoki.tipus = szavak[ind]
        if(ind+2<count):
            egy_csoki.tomeg = szavak[ind+1]
            egy_csoki.csomagolas = szavak[ind+2]
        csokik.append(egy_csoki)
        ind = ind+3
    
    for egy in csokik:
        print(f'{egy.tipus} , {egy.tomeg} , {egy.csomagolas}')
    