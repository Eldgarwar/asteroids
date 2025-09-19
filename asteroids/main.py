# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill((0, 0, 0))
        player.draw(screen)
        player.update(dt)

        pygame.display.flip()
        dt = clock.tick(60) / 1000  # Amount of seconds between each loop

if __name__ == "__main__":
    main()
