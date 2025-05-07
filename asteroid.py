from circleshape import *
import pygame
import random
import math
from constants import *
class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.points = self._generate_lumpy_points()
        self.colors = ["red", "blue" , "white", "green", "yellow"]
        self.color_choice = random.randint(0,4)
        

    def _generate_lumpy_points(self):
        """Generate points for a lumpy asteroid shape."""
        points = []
        num_points = random.randint(7, 12)  # Number of vertices
        
        for i in range(num_points):
            angle = 2 * math.pi * i / num_points
            # Random variation in radius (between 70% and 110% of base radius)
            variation = random.uniform(0.7, 1.2)
            distance = self.radius * variation
            # Calculate point position relative to center
            x = distance * math.cos(angle)
            y = distance * math.sin(angle)
            points.append((x, y))
            
        return points

    def draw(self, screen):
        # Transform the points to screen coordinates
        screen_points = []
        for x, y in self.points:
            screen_points.append((x + self.position.x, y + self.position.y))
        
        # Draw the lumpy asteroid

        pygame.draw.polygon(screen, self.colors[self.color_choice], screen_points, 4)
    
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

        
