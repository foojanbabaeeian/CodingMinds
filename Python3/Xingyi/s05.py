# I like to move it move it
# Music with Christina 
import pygame
import random


class Text():
    def __init__(self, surface, text, size, color, x, y):
        font_name = pygame.font.match_font('arial')
        self.surface = surface
        self.text = text
        self.size = size
        self.font = pygame.font.Font(font_name, self.size)
        self.color = color
        self.x = x
        self.y = y
    def draw(self):
        text_surface = self.font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (self.x, self.y)
        self.surface.blit(text_surface, text_rect)


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 500))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.mixer.music.load("bubble.mp3")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                # Draw a green rectangle at a random position
                pygame.draw.circle(screen, (0, 255, 255), (random.randint(1, 400), random.randint(1, 450)), 5)
                game_text.draw()
                pygame.mixer.music.play(2)
            elif event.key == pygame.K_a:
                pygame.draw.circle(screen, (255, 255, 0), (random.randint(1, 400), random.randint(1, 450)), 2)
                game_text.draw()
                pygame.mixer.music.play(2)
            elif event.key == pygame.K_s:
                pygame.draw.circle(screen, (0, 255, 0), (random.randint(1, 400), random.randint(1, 450)), 6)
                game_text.draw()
                pygame.mixer.music.play(2)
            elif event.key == pygame.K_d:
                pygame.draw.circle(screen, (255, 0, 255), (random.randint(1, 400), random.randint(1, 450)), 4)
                welcome.draw()
                pygame.mixer.music.play(2)
    game_text = Text(screen, "Hello Christina!", 20, (255, 0, 255), 250, 5)
    welcome = Text(screen, "I hope you are having fun in the class!", 20, (255, 0, 0), 250, 50)

    # game_text.draw()
    # welcome.draw()
    pygame.mixer.music.play(2)
    pygame.display.update()
    clock.tick(60)

    