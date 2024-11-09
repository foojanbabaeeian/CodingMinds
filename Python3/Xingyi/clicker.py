import pygame
import time
from os import path 

# Initialize Pygame
pygame.init()

# Variables and screen setup
count = 0
screen_width = 500
screen_height = 280
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Candy Clicker")

# Colors
black = (0, 0, 0)
turquoise = (138, 255, 239)

# Font setup
font_name = pygame.font.match_font('comic sans ms')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, black)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

# Game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
    # Check if the space bar is pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:  # If spacebar is pressed
        count += 1
        time.sleep(0.1)  # Short delay to avoid rapid counting
    
    # Fill screen background with turquoise color
    screen.fill(turquoise)
    
    # Draw a circle to represent the candy
    pygame.draw.circle(screen, black, (screen_width // 2, screen_height // 2), 50)
    
    # Display the current count
    draw_text(screen, "Candy: " + str(count), 30, screen_width / 2, screen_height / 20)
    
    # Update display
    pygame.display.update()
