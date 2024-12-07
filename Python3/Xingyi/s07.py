
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        

christina = Player()
player_group = pygame.sprite.Group()
player_group.add(christina)


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Christina vs Fooj")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()  
    screen.fill((0, 0, 0)) # fill in screen with bg color for every update 
    player_group.draw(screen)
    clock.tick(60)