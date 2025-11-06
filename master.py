import time
import random

# --- Játék beállítások ---
WIDTH = 40  # Tábla szélessége
HEIGHT = 20 # Tábla magassága

# Játék elemek jelölése
URES = ' '
FAL = '█'
LABDA = 'O'
UTO = '='

# --- Kezdeti állapot ---
def uj_tabla():
    """Létrehozza a játéktáblát és a falat."""
    tabla = [[URES for _ in range(WIDTH)] for _ in range(HEIGHT)]
    
    # Fal létrehozása (a tábla felső 4 sora)
    for y in range(4):
        for x in range(WIDTH):
            if x % 3 != 1: # Kihagyunk néhány helyet a változatosság kedvéért
                tabla[y][x] = FAL
                
    return tabla

# --- Labda és Ütő állapot ---
class JatekAllapot:
    def __init__(self):
        self.tabla = uj_tabla()
        self.score = 0
        self.lives = 3
        
        # Labda pozíció és sebesség (dx/dy)
        self.ball_x = WIDTH // 2
        self.ball_y = HEIGHT - 3
        self.ball_dx = random.choice([-1, 1])
        self.ball_dy = -1 # Labda felfelé indul
        
        # Ütő pozíció
        self.paddle_x = WIDTH // 2 - 4
        self.PADDLE_SIZE = 8
        
        # Játék futásának állapota
        self.running = True

def tabla_megjelenit(state):
    """Kiírja a táblát és az aktuális állapotot a konzolra."""
    
    # Képernyő törlése (egyszerű módja)
    print("\033c", end="") 
    
    # Állapot kiírása
    print(f"💰 Pontszám: {state.score} | ❤️ Életek: {state.lives} | Kilépés: Q")
    print("-" * (WIDTH + 2))
    
    # A tábla kirajzolása
    for y in range(HEIGHT):
        sor = "|"
        for x in range(WIDTH):
            # Ütő kirajzolása
            if y == HEIGHT - 1 and state.paddle_x <= x < state.paddle_x + state.PADDLE_SIZE:
                sor += UTO
            # Labda kirajzolása
            elif x == state.ball_x and y == state.ball_y:
                sor += LABDA
            # Fal/Üres kirajzolása
            else:
                sor += state.tabla[y][x]
        sor += "|"
        print(sor)
        
    print("-" * (WIDTH + 2))

def mozgatas(state):
    """Mozgatja a labdát és kezeli az ütközéseket."""
    
    next_x = state.ball_x + state.ball_dx
    next_y = state.ball_y + state.ball_dy
    
    # --- Ütközés a tábla szélével ---
    # Bal/Jobb fal
    if next_x <= 0 or next_x >= WIDTH - 1:
        state.ball_dx *= -1
        next_x = state.ball_x + state.ball_dx
        
    # Felső fal
    if next_y <= 0:
        state.ball_dy *= -1
        next_y = state.ball_y + state.ball_dy

    # Alsó terület (elvesztett élet)
    if next_y >= HEIGHT - 1:
        state.lives -= 1
        if state.lives > 0:
            # Labda visszaállítása
            state.ball_x = WIDTH // 2
            state.ball_y = HEIGHT - 3
            state.ball_dy = -1
        else:
            state.running = False
            return

    # --- Ütközés az ÜTŐVEL ---
    # Ha a labda az ütő pozíciójában van
    if next_y == HEIGHT - 1:
         if state.paddle_x <= next_x < state.paddle_x + state.PADDLE_SIZE:
             state.ball_dy *= -1
             # Kis sebesség változtatás a realisztikusabb hatásért
             center = state.paddle_x + state.PADDLE_SIZE / 2
             if next_x < center - 1:
                 state.ball_dx = -1
             elif next_x > center + 1:
                 state.ball_dx = 1
             else:
                 state.ball_dx = random.choice([-1, 1])

             next_y = state.ball_y + state.ball_dy # Frissítsük az y pozíciót az új sebességgel
             
    # --- Ütközés a FALLAL ---
    if state.tabla[next_y][next_x] == FAL:
        state.tabla[next_y][next_x] = URES # Töröljük a téglát
        state.ball_dy *= -1                # Irányváltás
        state.score += 10                  # Pontszám növelése
        
        # Ellenőrizzük, hogy maradt-e tégla
        if all(FAL not in sor for sor in state.tabla):
            print("\n** GRATULÁLOK! MINDEN TÉGLÁT LEÜTÖTTÉL! **")
            state.running = False

    # Új labda pozíció beállítása
    state.ball_x += state.ball_dx
    state.ball_y += state.ball_dy
    
def kezeles(state, key):
    """Kezeli a felhasználói bevitelt az ütő mozgatásához."""
    if key == 'a':
        state.paddle_x = max(0, state.paddle_x - 4)
    elif key == 'd':
        state.paddle_x = min(WIDTH - state.PADDLE_SIZE, state.paddle_x + 4)
    elif key == 'q':
        state.running = False

def jatek_futtat():
    """A játék fő ciklusa."""
    state = JatekAllapot()
    
    # A bemenet kezeléséhez Linux/macOS alatt a 'curses' ideális lenne.
    # Egyszerű konzolos szimulációhoz a Python 'input()' blokkoló, 
    # ezért a játék sebessége függ attól, milyen gyorsan adsz meg parancsot.
    print("--- 🧱 Faltörő (Breakout) Szimuláció ---")
    print("Használd az 'a' (balra) és 'd' (jobbra) gombokat.")
    print("Minden billentyűleütés után nyomj ENTER-t a teszt kedvéért.")
    print("A labda minden ENTER után lép egyet.")
    
    while state.running:
        tabla_megjelenit(state)
        
        # Bemenet kérése (ez blokkolja a programot)
        command = input("Lépés (a/d/q) + ENTER: ").lower()
        
        kezeles(state, command)
        
        if state.running:
            mozgatas(state)
            # time.sleep(0.05) # Kis késleltetés, ha nem blokkoló inputot használsz

    # Játék vége
    print("\n--- A JÁTÉK VÉGE ---")
    if state.lives == 0:
        print("😞 Játék vége. Elfogyott az életed.")
    print(f"Végső pontszám: {state.score}")

# Indítsuk el a játékot
if __name__ == "__main__":
    jatek_futtat()