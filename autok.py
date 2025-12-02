class Auto:
    def __init__(self,gyarto="",tipus="",uzemanyag=""):
        self.gyarto = gyarto
        self.tipus = tipus
        self.uzemanyag = uzemanyag

    def Uzemanyag(self):
        match self.uzemanyag:
            case 'd':
                return 'dízel'
            case 'b':
                return 'benzin'
            case _:
                return 'nem tudom milyen'

#main
autok = []
for _ in range(3):
    auto = Auto()
    auto.gyarto = input('Add meg egy autó márkáját: ')
    auto.tipus = input('Add meg egy autó model típusát: ')
    auto.uzemanyag = input('Add meg az üzemanyag típusát (d/b): ')
    autok.append(auto)

for auto in autok:
    print(f'A(z) {auto.gyarto} {auto.tipus} {auto.Uzemanyag()} üzemű')