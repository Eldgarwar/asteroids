import random
from constants import *
import pygame # type: ignore
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)  # Asteroids start stationary

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def split(self):
        if self.radius > ASTEROID_MIN_RADIUS:
            for _ in range(2):  # Split into 2 smaller asteroids
                new_radius = self.radius - ASTEROID_MIN_RADIUS
                new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
                new_velocity = self.velocity.rotate(random.uniform(-50, 50)) * random.uniform(1.2, 1.5)
                new_asteroid.velocity = new_velocity
                self.groups()[0].add(new_asteroid)  # Add to the same group as the original asteroid
        self.kill()  # Remove the original asteroid

    def update(self, dt):
        self.position += self.velocity * dt

        # Wrap around screen edges
        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        elif self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = SCREEN_HEIGHT
        elif self.position.y > SCREEN_HEIGHT:
            self.position.y = 0