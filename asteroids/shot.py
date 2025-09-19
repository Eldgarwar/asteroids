from constants import *
import pygame # type: ignore
from circleshape import CircleShape


class Shot(CircleShape):
    instances = []

    def __init__(self, x, y, rotation):
        super().__init__(x, y, BULLET_RADIUS)
        self.rotation = rotation
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.velocity = forward * BULLET_SPEED
        Shot.instances.append(self)

    def kill(self):
        try:
            Shot.instances.remove(self)
        except ValueError:
            pass
        super().kill()

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

