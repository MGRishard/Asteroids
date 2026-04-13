import random
import pygame
from circleshape import CircleShape
from logger import log_event
from constants import LINE_WIDTH,ASTEROID_MIN_RADIUS
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self,screen):
        pygame.draw.circle(screen,"white", self.position, self.radius, LINE_WIDTH)
    def update(self,dt):
        self.position += self.velocity * dt 
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)

        # Create two new velocity vectors by rotating the current one
        # .rotate() is a method available on pygame.Vector2
        vel_1 = self.velocity.rotate(random_angle)
        vel_2 = self.velocity.rotate(-random_angle)

        # Compute the new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # 4. Spawn two new asteroids at the current position
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        # 5. Set their velocity and increase speed by 1.2x
        asteroid1.velocity = vel_1 * 1.2
        asteroid2.velocity = vel_2 * 1.2
