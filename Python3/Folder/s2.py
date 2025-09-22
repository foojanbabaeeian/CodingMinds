import pygame

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((500, 500))

pygame.mixer.music.load("The Duck Song.mp3")

# print("The Duck Song")

pygame.mixer.music.play(1)

class Albert(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
    def update(self):
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_UP]:
            self.rect.y -= 5
        elif keystate[pygame.K_DOWN]:
            self.rect.y += 5
            
class Kai(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 5
        if self.rect.left > 500:
            self.rect.right = 0

kai_image = pygame.image.load("kai.png")
albert_image = pygame.image.load("albert.png")



while True:
    
    screen.fill((0,0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    


    
    pygame.display.update()
    clock.tick(60)