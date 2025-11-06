import random

#global valasz
#global rejtett

tipp_szam = 0

def colored(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

def tipp_megtesz(input_str, random_sample):
    rejtett = random_sample[0]+random_sample[1]+random_sample[2]+random_sample[3]+random_sample[4]
    valasz = ""
    if input_str[0] == random_sample[0]:
        valasz = valasz + input_str[0]
    elif input_str[0] in rejtett:
        valasz = valasz + "X"
    else:
        valasz = valasz + "O"
    if input_str[1] == random_sample[1]:
        valasz = valasz + input_str[1]
    elif input_str[1] in rejtett:
        valasz = valasz + "X"
    else:
        valasz = valasz + "O"
    if input_str[2] == random_sample[2]:
        valasz = valasz + input_str[2]
    elif input_str[2] in rejtett:
        valasz = valasz + "X"
    else:
        valasz = valasz + "O"
    if input_str[3] == random_sample[3]:
        valasz = valasz + input_str[3]
    elif input_str[3] in rejtett:
        valasz = valasz + "X"
    else:
        valasz = valasz + "O"
    if input_str[4] == random_sample[4]:
        valasz = valasz + input_str[4]
    elif input_str[4] in rejtett:
        valasz = valasz + "X"
    else:
        valasz = valasz + "O"
    
    return jatek_vege(rejtett,valasz)

def valasz_colorize(rejtett,valasz):
    red_P = colored(255, 0, 0, "P")
    blue_K = colored(0, 0, 255, "K")
    green_Z = colored(0, 255, 0, "Z")
    yellow_S = colored(255, 255, 0, "S")
    
    valasz0 = valasz[0]
    match valasz[0]:
        case "P":
            valasz0 = red_P
        case "K":
            valasz0 = blue_K
        case "Z":
            valasz0 = green_Z
        case "S":
            valasz0 = yellow_S
    
    valasz1 = valasz[1]
    match valasz[1]:
        case "P":
            valasz1 = red_P
        case "K":
            valasz1 = blue_K
        case "Z":
            valasz1 = green_Z
        case "S":
            valasz1 = yellow_S
    
    valasz2 = valasz[2]
    match valasz[2]:
        case "P":
            valasz2 = red_P
        case "K":
            valasz2 = blue_K
        case "Z":
            valasz2 = green_Z
        case "S":
            valasz2 = yellow_S
    
    valasz3 = valasz[3]
    match valasz[3]:
        case "P":
            valasz3 = red_P
        case "K":
            valasz3 = blue_K
        case "Z":
            valasz3 = green_Z
        case "S":
            valasz3 = yellow_S
    
    valasz4 = valasz[4]
    match valasz[4]:
        case "P":
            valasz4 = red_P
        case "K":
            valasz4 = blue_K
        case "Z":
            valasz4 = green_Z
        case "S":
            valasz4 = yellow_S
    
    print(valasz0+" "+valasz1+" "+valasz2+" "+valasz3+" "+valasz4)
    

def jatek_vege(rejtett,valasz):
    global tipp_szam
    global newgame_str
    tipp_szam = tipp_szam + 1
    if valasz == rejtett:
        #print("!!!GYŐZTÉL!!!")
        valasz_colorize(rejtett,valasz)
        win_string = "!!!GYŐZTÉL!!!  "+str(tipp_szam)+" kör alatt"
        print(colored(255, 0, 0, win_string))
        print(colored(0, 0, 255, win_string))
        print(colored(0, 255, 0, win_string))
        print(colored(255, 255, 0, win_string))

        # új játék
        newgame_str = ""
        newgame_str = input(f"Játszol mégegyet? (Y): ")
        newgame_str = newgame_str.upper()
        return True
    else:
        valasz_colorize(rejtett,valasz)
        return False

def main():
    global tipp_szam
    tipp_szam = 0
    red_P = colored(255, 0, 0, "P")
    blue_K = colored(0, 0, 255, "K")
    green_Z = colored(0, 255, 0, "Z")
    yellow_S = colored(255, 255, 0, "S")

    #játékszabály            
    print("négy bábu szín: piros ("+red_P+"), kék ("+blue_K+"), zöld ("+green_Z+"), sárga ("+yellow_S+")")
    print("5 rejtett bábu")
    print("jó helyen jó szín - (P,K,Z,S), jó szín rossz helyen 'X', rossz szín 'O'")
    
    elements = ["P", "K", "Z", "S","P", "K", "Z", "S","P", "K", "Z", "S"]
    #for i in range(5):
    random_sample = random.sample(elements, 5)
    print("Kezdődhet a játék:")
    #print(f"{random_sample}")
    rejtett = random_sample[0]+random_sample[1]+random_sample[2]+random_sample[3]+random_sample[4]
    #print(rejtett)
    
    print(rejtett)
    
    tipp_ervenyes = False
    while not tipp_ervenyes:
        try:
            # bekérjük a tippet
            input_str = input(f"Add meg a tipped (pl. KKSPZ): ")
            input_str = input_str.upper()
            if len(input_str) != 5:
                raise ValueError
            
            if input_str[0] in "PKZS" and input_str[1] in "PKZS" and input_str[2] in "PKZS" and input_str[3] in "PKZS" and input_str[4] in "PKZS":
                tipp_ervenyes = tipp_megtesz(input_str, random_sample)
            else:
                print("Érvénytelen tipp. Próbáld újra!")
        except ValueError:
            print("Hibás formátum. Kérlek, öt betűt adj meg (pl. PKZSP).")

main()
if newgame_str == "Y":
    newgame_str = ""
    main()