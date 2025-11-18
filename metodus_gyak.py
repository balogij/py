def rovidebb_eljaras(szo_1,szo_2):
    if(len(szo_1)>len(szo_2)):
        return "az első szó a hosszabb"
    elif(len(szo_1)<len(szo_2)):
        return "a második szó a hosszabb"
    elif(len(szo_1)==len(szo_2)):
        return "a két szó egyenlő hosszúságú"        
    
#main
rossz_ertek = True
while(rossz_ertek):
    try:
        szo_1 = str(input("Add meg az első szót: "))
        rossz_ertek = False
    except:
        print("ez nem szó")

rossz_ertek = True
while(rossz_ertek):
    try:
        szo_2 = str(input("Add meg az első szót: "))
        rossz_ertek = False
    except:
        print("ez nem szó")
print(f"válasz: {rovidebb_eljaras(szo_1,szo_2)}")
