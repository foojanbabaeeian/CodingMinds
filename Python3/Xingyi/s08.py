import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Debug")

enemy = Enemy()
player_group = pygame.sprite.Group()
player_group.add(enemy)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill((0, 0, 0))
    player_group.draw(screen)
    pygame.display.update()
    clock.tick(60)
