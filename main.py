import pygame
from player import Player
from logger import log_state
from constants import *
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dv = 0
    while True:
        log_state()
        for event in pygame.event.get():
            pass
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        dv = clock.tick(60)/1000
        player.update(dv)
  #      print(dv)
    print("Starting Asteroids with pygame version: 2.6.1")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
