# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame # type: ignore
from constants import *
from player import Player
from shot import Shot
from asteroidfield import AsteroidField
from asteroid import Asteroid

def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    # sprite groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()

    # set class-level containers before creating instances so sprites auto-add
    Player.containers = updateable, drawable
    Asteroid.containers = asteroid, updateable, drawable
    Shot.containers = updateable, drawable
    AsteroidField.containers = updateable

    # create game objects
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    asteroidfield = AsteroidField()

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

        # update all updateable sprites (includes asteroidfield which spawns asteroids)
        updateable.update(dt)

        # check for collisions
        for a in asteroid:
            if player.collide(a):
                print("Game over!")
                pygame.quit()
                return
            for s in Shot.instances:
                if s.collide(a):
                    a.split()
                    s.kill()
                    break 
        # draw all drawable sprites
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000  # Amount of seconds between each loop

if __name__ == "__main__":
    main()
