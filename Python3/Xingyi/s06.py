import pygame
import random

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (250, 250)
        self.speed = 5
    def update(self, keys):
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        self.rect.x = max(0, min(500 - self.rect.width, self.rect.x))
        self.rect.y = max(0, min(500 - self.rect.height, self.rect.y))

christina = Player()
boo = Player()
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 400)
        self.rect.y = random.randint(0, 400)
        self.speed = 2
    def update(self, keys):
        self.rect.x += self.speed
        self.rect.y += self.speed
        self.rect.x = max(0, min(500 - self.rect.width, self.rect.x))
        self.rect.y = max(0, min(500 - self.rect.height, self.rect.y))

fooj = Enemy()


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Christina vs Fooj")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    keys = pygame.key.get_pressed()
    
    christina.update(keys)
    fooj.update(keys)
    screen.blit(christina.image, christina.rect)  # Draw player
    screen.blit(fooj.image, fooj.rect)  # Draw enemy
    
    pygame.display.update()
    clock.tick(60)

    