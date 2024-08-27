import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basic Particle Physics Engine")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Define a Particle class
class Particle:
    def __init__(self, x, y, vx, vy, radius):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.gravity = 0.1  # Gravity acceleration

    def update(self):
        # Update velocity with gravity
        self.vy += self.gravity
        # Update position with velocity
        self.x += self.vx
        self.y += self.vy
        
        # Check for collision with the edges
        if self.x - self.radius < 0 or self.x + self.radius > WIDTH:
            self.vx *= -0.8  # Reflect velocity and lose some speed
        if self.y - self.radius < 0 or self.y + self.radius > HEIGHT:
            self.vy *= -0.8  # Reflect velocity and lose some speed
        
        # Ensure particle stays within bounds
        self.x = max(self.radius, min(WIDTH - self.radius, self.x))
        self.y = max(self.radius, min(HEIGHT - self.radius, self.y))

    def draw(self, screen):
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), self.radius)

# Main loop
def main():
    clock = pygame.time.Clock()
    particles = [Particle(random.randint(0, WIDTH), random.randint(0, HEIGHT), random.uniform(-2, 2), random.uniform(-2, 2), 5) for _ in range(50)]
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update particles
        for particle in particles:
            particle.update()
        
        # Draw everything
        screen.fill(BLACK)
        for particle in particles:
            particle.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)  # Cap the frame rate at 60 FPS
    
    pygame.quit()

if __name__ == "__main__":
    main()
