import random

#Tanulok = ['István','Géze','Edina',"Éva",'Ádám']
#Azonositok =[12,13,14,15,16]
#Ertekelesek = [2,5,4,3,2,1]
#print(Tanulok)
#print(Azonositok)
#print(Ertekelesek)

#for t_index in range(len(Tanulok)):
#    print(f"Név:  {Tanulok[t_index]},   Azonosító: {Azonositok[t_index]},   Értékelés: {Ertekelesek[t_index]}")

class Tanulok:
    def __init__(self, name, id, score):
        self.name = name
        self.id = id
        self.score = score


#t_lista = [Tanulok('Istvan',12,2),Tanulok('Géza',13,5),Tanulok('Edina',14,3),Tanulok('Éva',15,2),Tanulok('Ádám',16,1)]

#max = len(t_lista)
lottoszamok = []

for i in range(5):
    #tanulo = t_lista[random.randrange(0,max)]
    #print(f"ID: {tanulo.id} Név: {tanulo.name} Értékelés: {tanulo.score}")
    veletlenszam = random.randrange(1,91)        
    if(veletlenszam not in lottoszamok):
        lottoszamok.append(veletlenszam)    

rendezett = sorted(lottoszamok)
print(rendezett)