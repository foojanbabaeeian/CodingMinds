import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        
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

# create sprite objects
player = Player() 
opponent1 = Player()
opponent2 = Player()

# create sprite group
opponent_group = pygame.sprite.Group()
opponent_group.add(opponent1)
opponent_group.add(opponent2)

# save list of collided sprites into a variable
hit_list = pygame.sprite.spritecollide(player, opponent_group, False)

# iterate through list
for hit in hit_list:
  print("Collided!")

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Collision Detection")

# enemy = Enemy()
# player_group = pygame.sprite.Group()
# player_group.add(enemy)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    # if pygame.sprite.collide_rect(player1, player2):
    #     print("Coliddedddddd!!!!!!")

    screen.fill((0, 0, 0))
    # player_group.draw(screen)
    pygame.display.update()
    clock.tick(60)
