import random

## 🍫 Csoki osztály definíciója
class Csoki:
    def __init__(self, tipus, tomeg, csomagolas):
        self.tipus = tipus
        self.tomeg = tomeg
        self.csomagolas = csomagolas

    def Ar(self):
        # Ez a metódus visszaadja a csoki árát a tömeg alapján
        alap_ar = self.tomeg * 3  # Alapár: 3 Ft/g
        ar_novekedes = 0
        match self.csomagolas:
            case "papír":
                ar_novekedes = 100
            case "doboz":
                ar_novekedes = 500
            case _:
                ar_novekedes = 0
        return alap_ar + ar_novekedes

    def __str__(self):
        # Ez a metódus határozza meg, hogyan jelenjen meg az objektum kiíráskor
        tipus = self.tipus
        while(len(tipus)<5):
            tipus += " "
        csomaolas = self.csomagolas
        while(len(csomaolas)<7):
            csomaolas += " "
        tomeg = str(self.tomeg)
        while(len(tomeg)<3):
            tomeg = " " + tomeg
        return f"Típus: {tipus}, Tömeg: {tomeg}g, Csomagolás: {csomaolas} -> Ár: {self.Ar()}-Ft"

# ---

## 💾 Fájl írása és adatok generálása
def rekordok_generalasa_es_irasa(fajlnev="csokibolt.txt", darabszam=20):
    """Generál véletlenszerű csoki adatokat, és kiírja azokat a megadott fájlba."""
    
    # Lehetséges értékek a random generáláshoz
    tipusok = ["ét", "tej", "fehér"]
    tomegek = list(range(50, 251, 10)) # 50-250g között, 10g-os lépésekkel
    csomagolasok = ["kimérős", "papír", "doboz"]
    
    print(f"**Generálok {darabszam} véletlenszerű csoki rekordot a(z) '{fajlnev}' fájlba...**")

    try:
        # A 'w' mód felülírja a fájlt, ha létezik, és létrehozza, ha nem
        with open(fajlnev, 'w', encoding='utf-8') as f:
            for _ in range(darabszam):
                # Véletlenszerűen választunk értékeket
                tipus = random.choice(tipusok)
                tomeg = random.choice(tomegek)
                csomagolas = random.choice(csomagolasok)
                
                # A rekordot ';'-vel elválasztva írjuk a fájlba
                rekord = f"{tipus};{tomeg};{csomagolas}\n"
                f.write(rekord)
        
        print(f"Sikeresen kiírva {darabszam} rekord a(z) '{fajlnev}' fájlba.")
        
    except IOError as e:
        print(f"Hiba történt a fájl írásakor: {e}")

# ---

## 📂 Fájl olvasása és lista feltöltése
def lista_feltoltese_a_fajlbol(fajlnev="csokibolt.txt"):
    """Beolvassa a fájl tartalmát, és Csoki típusú objektumokat tartalmazó listát készít belőle."""
    
    csoki_lista = []
    print(f"\n**Beolvasom a rekordokat a(z) '{fajlnev}' fájlból és feltöltöm a listát...**")
    
    try:
        # A 'r' mód a fájl olvasására szolgál
        with open(fajlnev, 'r', encoding='utf-8') as f:
            # Végigmegyünk a fájl minden során
            for sor in f:
                # Eltávolítjuk a sortörést és szétdaraboljuk a ';' mentén
                adatok = sor.strip().split(';')
                
                # Ellenőrizzük, hogy pontosan 3 adatunk van-e
                if len(adatok) == 3:
                    tipus = adatok[0]
                    # A tömeget stringből int-té kell konvertálni
                    try:
                        tomeg = int(adatok[1])
                    except ValueError:
                        print(f"Figyelem: Érvénytelen tömeg adat kihagyva: {adatok[1]}")
                        continue # Ugrás a következő sorra
                        
                    csomagolas = adatok[2]
                    
                    # Létrehozzuk a Csoki objektumot és hozzáadjuk a listához
                    csoki = Csoki(tipus, tomeg, csomagolas)
                    csoki_lista.append(csoki)
            f.close() 
        print(f"Sikeresen beolvasva {len(csoki_lista)} csoki objektum.")
        return csoki_lista
        
    except FileNotFoundError:
        print(f"Hiba: A '{fajlnev}' fájl nem található.")
        return []
    except IOError as e:
        print(f"Hiba történt a fájl olvasásakor: {e}")
        return []

# ---

## 🖥️ Lista kiírása a képernyőre
def lista_kiirasa(lista):
    """Kiírja a listában lévő összes Csoki objektumot."""
    
    if not lista:
        print("\n**A lista üres, nincs mit kiírni.**")
        return
        
    print("\n**A feltöltött csoki listában lévő elemek:**")
    print("------------------------------------------")
    
    # Végigmegyünk a listán és kiírjuk az objektumokat
    for i, csoki in enumerate(lista):
        # A Csoki osztályban definiált __str__ metódus fogja formázni a kiírást
        if i < 9:
            print(f" {i+1}. {csoki}")
        else:
            print(f"{i+1}. {csoki}")
    print("------------------------------------------")


# 🚀 Fő program futtatása
if __name__ == "__main__":
    
    fajl_nev = "csokibolt.txt"
    
    # 1. Rekordok generálása és fájlba írása
    rekordok_generalasa_es_irasa(fajl_nev)
    
    # 2. Fájl olvasása és lista feltöltése
    csoki_objektumok = lista_feltoltese_a_fajlbol(fajl_nev)
    
    # 3. Lista elemeinek kiírása
    lista_kiirasa(csoki_objektumok)