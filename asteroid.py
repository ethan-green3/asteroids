from circleshape import *
import pygame
import random
from constants import *
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        postive_rotation = self.velocity.rotate(angle)
        negative_rotation = self.velocity.rotate(-angle)

        self.radius = self.radius - ASTEROID_MIN_RADIUS
        first_asteroid = Asteroid(self.position.x, self.position.y, self.radius)
        second_asteroid = Asteroid(self.position.x, self.position.y, self.radius)

        first_asteroid.velocity = postive_rotation * 1.2
        second_asteroid.velocity = negative_rotation * 1.2

        Asteroid.add(first_asteroid)
        Asteroid.add(second_asteroid)

        
