import pygame
import sys
import random

# --- Inicializálás ---
pygame.init()

# --- Ablak Beállítások ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Python Invaders")

# --- Színek ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# --- Játékos (Űrhajó) Osztály ---
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Egy egyszerű fehér négyzet a játékos
        self.image = pygame.Surface([50, 50])
        self.image.fill(WHITE) 
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2 - 25
        self.rect.y = SCREEN_HEIGHT - 70
        self.speed = 5

    def update(self, keys):
        # Mozgás balra és jobbra a billentyűzet segítségével
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

# --- Fő Játék Ciklus ---
def game_loop():
    running = True
    clock = pygame.time.Clock()
    
    # Sprite csoportok
    all_sprites = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)

    while running:
        # 1. Eseménykezelés (Input)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # TODO: Lövés események kezelése itt

        # Billentyűzet állapotának lekérdezése
        keys = pygame.key.get_pressed()
        
        # 2. Játékállapot Frissítése
        all_sprites.update(keys)

        # 3. Képernyő Rajzolása
        screen.fill(BLACK) # Fekete háttér
        all_sprites.draw(screen) # Sprite-ok rajzolása
        
        # TODO: Ellenségek, lövedékek és pontszám rajzolása itt
        
        # Képernyő frissítése
        pygame.display.flip()

        # Játék sebességének beállítása (FPS)
        clock.tick(60) 

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game_loop()