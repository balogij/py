class Csoki:
    def __init__(self, tipus, tomeg, csomagolas):
        self.tipus = tipus
        self.tomeg = tomeg
        self.csomagolas = csomagolas

    def Ar(self):
        alap_ar = self.tomeg * 3
        ar_novekedes = 0
        match self.csomagolas:
            case "papír":
                ar_novekedes = 100
            case "doboz":
                ar_novekedes = 500
            case _:
                ar_novekedes = 0
        return alap_ar + ar_novekedes