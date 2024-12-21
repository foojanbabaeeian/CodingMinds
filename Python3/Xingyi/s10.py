import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class Player(pygame.sprite.Sprite):
    def __init__(self,image, scale, x, y):
        pygame.sprite.Sprite.__init__(self)
        width = image.get_width()  
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))

        # self.image = pygame.Surface((50, 50))
        # self.image.fill((0, 0, 255))
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
playerimage = pygame.image.load("Python3/Xingyi/images/player.jpg")
# Create sprite objects
player = Player(playerimage, 0.15, 0, 0)

player_group = pygame.sprite.Group()
player_group.add(player)  # add player object to player group

opponent1 = Enemy(100, 100)  # Set initial position
opponent2 = Enemy(300, 300)  # Set initial position

# Create sprite group for opponents
opponent_group = pygame.sprite.Group()
opponent_group.add(opponent1, opponent2)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    player_group.draw(screen)
    keys = pygame.key.get_pressed()
    player.update(keys)

    # Check for collisions
    hit_list = pygame.sprite.spritecollide(player, opponent_group, False)
    for hit in hit_list:
        print("Collided!")

    # Draw everything
    screen.fill((0, 0, 0))
    screen.blit(player.image, player.rect)
    opponent_group.draw(screen)
    pygame.display.update()

    clock.tick(60)
