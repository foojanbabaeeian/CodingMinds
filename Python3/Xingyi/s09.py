import pygame
import random
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (random.randint(0,500), random.randint(0,500))
        
class Ability(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((44,255,5))
        self.rect = self.image.get_rect()
        self.rect.topleft = (random.randint(0,500), random.randint(0,500))

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


# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Collision Detection")
clock = pygame.time.Clock()

# Create sprite objects
player = Player()
opponent1 = Enemy()  # Set initial position
opponent2 = Enemy()  # Set initial position
opponent3 = Enemy()

ability = Ability()
ability_group = pygame.sprite.Group()
ability_group.add(ability)

# Create sprite group for opponents
opponent_group = pygame.sprite.Group()
opponent_group.add(opponent1, opponent2, opponent3)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()
    player.update(keys)

    # Check for collisions
    hit_list = pygame.sprite.spritecollide(player, opponent_group, False)
    for hit in hit_list:
        print("Wompity Womp!")
        pygame.quit()
        quit()
    hit_list = pygame.sprite.spritecollide(player, ability_group, False)
    for hit in hit_list:
        print("yayi!")

    # Draw everything
    screen.fill((0, 0, 0))
    screen.blit(player.image, player.rect)
    opponent_group.draw(screen)
    ability_group.draw(screen)

    pygame.display.update()

    clock.tick(60)
