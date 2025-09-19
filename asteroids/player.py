from constants import *
from circleshape import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0  # in degrees

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def rotate(self, direction, dt):
        if direction == "left":
            self.rotation -= PLAYER_TURN_SPEED * dt
        elif direction == "right":
            self.rotation += PLAYER_TURN_SPEED * dt
        self.rotation %= 360  # keep it in the range [0, 360)

    def move(self, direction, dt):
        if direction == "forward":
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            self.position += forward * PLAYER_MOVE_SPEED * dt
        elif direction == "backward":
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            self.position -= forward * PLAYER_MOVE_SPEED * dt

        # Wrap around screen edges
        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        elif self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = SCREEN_HEIGHT
        elif self.position.y > SCREEN_HEIGHT:
            self.position.y = 0     
            

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate("left", dt)
        if keys[pygame.K_d]:
            self.rotate("right", dt)
        if keys[pygame.K_w]:
            self.move("forward", dt)
        if keys[pygame.K_s]:
            self.move("backward", dt)