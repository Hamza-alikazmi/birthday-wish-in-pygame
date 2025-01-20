import pygame
import random
import math
import sys

# Initialize Pygame
pygame.init()

# Set screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Realistic Fireworks and Birthday Cake")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (138, 43, 226)]

# Firework class
class Firework:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.particles = []
        self.create_particles()

    def create_particles(self):
        num_particles = random.randint(50, 100)
        for _ in range(num_particles):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(2, 6)
            vx = math.cos(angle) * speed
            vy = math.sin(angle) * speed
            color = random.choice(COLORS)
            lifetime = random.randint(20, 40)
            self.particles.append(Particle(self.x, self.y, vx, vy, color, lifetime))

    def update(self):
        for particle in self.particles:
            particle.update()

        # Remove particles that are out of screen or have expired
        self.particles = [p for p in self.particles if p.lifetime > 0]

    def draw(self, screen):
        for particle in self.particles:
            particle.draw(screen)

# Particle class
class Particle:
    def __init__(self, x, y, vx, vy, color, lifetime):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.lifetime = lifetime

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.lifetime -= 1

    def draw(self, screen):
        if self.lifetime > 0:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 3)

# Draw a more realistic birthday cake using pygame
def draw_cake():
    # Cake base (with a gradient effect to make it look more 3D)
    pygame.draw.rect(screen, (255, 182, 193), (150, 400, 500, 150))  # Pink base (larger bottom)
    pygame.draw.rect(screen, (255, 105, 180), (175, 405, 450, 140))  # Darker shade for 3D effect

    # Cake layers with gradient effect (upper layer smaller than the bottom)
    pygame.draw.rect(screen, (255, 255, 255), (175, 370, 450, 30))  # White top layer
    pygame.draw.rect(screen, (245, 245, 245), (175, 340, 450, 30))  # Slightly darker
    pygame.draw.rect(screen, (210, 210, 240), (220, 310, 310, 30))  # Slightly darker

    # Cake candles (colored rectangles)
    candle_colors = [(255, 0, 0), (0, 0, 255), (255, 255, 0), (0, 255, 0), (255, 165, 0)]
    for i, color in enumerate(candle_colors):
        pygame.draw.rect(screen, color, (250 + (i * 60), 290, 10, 30))  # Candles

    # Cake flames (yellow circles on top of the candles, with a subtle effect)
    for i in range(5):
        flame_y = 290 - random.randint(2, 5)
        flame_size = random.randint(4, 10)
        pygame.draw.circle(screen, (255, 255, 0), (255 + (i * 60), flame_y), flame_size)  # Flames

    # Birthday text with emojis
    font = pygame.font.SysFont("arial", 40)  # Try using a more common font
    text = font.render("Qutab!", True, (255, 255, 255))  # Added emojis directly in the string
    screen.blit(text, (WIDTH // 3, 50))  # Position the text at the top

# Main game loop to run fireworks and messages on click
def run_fireworks():
    fireworks = []  # List to hold active fireworks
    clock = pygame.time.Clock()
    messages = ["Happy", "Birthday", "To You", " "]  # Messages to display after each firework
    message_index = 0  # Start with the first message
    running = True

    while running:
        screen.fill(BLACK)  # Fill the screen with black

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button click
                    if message_index < len(messages):
                        # Create a new firework at the mouse position
                        mouse_x, mouse_y = event.pos
                        fireworks.append(Firework(mouse_x, mouse_y))
                        message_index += 1  # Move to the next message

        # Update and draw all fireworks
        for firework in fireworks:
            firework.update()
            firework.draw(screen)

        # If there are messages left to show, display the current message
        if message_index <= len(messages):
            if message_index > 0:  # Only display message if the index is greater than 0
                font = pygame.font.SysFont("Verdana", 40)
                text = font.render(messages[message_index - 1], True, (255, 255, 255))
                screen.blit(text, (WIDTH // 3, HEIGHT // 2))  # Display text in the center

        # Draw the cake after all messages are displayed
        if message_index == len(messages):
            draw_cake()

        pygame.display.flip()  # Update the display
        clock.tick(60)  # 60 FPS

    pygame.quit()  # Quit pygame when the loop ends

# Start the fireworks sequence on mouse click
run_fireworks()

