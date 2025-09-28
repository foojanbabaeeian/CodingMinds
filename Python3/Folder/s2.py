import pygame
import random


pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((500, 500))

pygame.mixer.music.load("The Duck Song.mp3")

# print("The Duck Song")

pygame.mixer.music.play(1)



class Alberta(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        width = image.get_width()  
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * 0.1), int(height * 0.1)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        keystate = pygame.key.get_pressed()
        
        if keystate[pygame.K_UP]:
            self.rect.y -= 5
        elif keystate[pygame.K_DOWN]:
            self.rect.y += 5




class Kaitherine(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * 0.5), int(height * 0.5)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x -= 5
        if self.rect.right < 0:
            self.rect.left = 500
            self.rect.y = random.randint(0, 470)

kai_image = pygame.image.load("kai.png")
albert_image = pygame.image.load("albert.png")

# I would like you to change where alberta and kai start

Albertata = Alberta(albert_image, 100, 100)
Alberta_group = pygame.sprite.Group()
Alberta_group.add(Albertata)


kai = Kaitherine(kai_image, 200, 200)
kai_group = pygame.sprite.Group()
kai_group.add(kai)

#  :D
while True:
    
    screen.fill((0,0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    Alberta_group.draw(screen)
    Alberta_group.update()

    kai_group.draw(screen)
    kai_group.update()

    pygame.display.update()
    # save list of collided sprites into a variable
    hit_list = pygame.sprite.spritecollide(Albertata, kai_group, False)

    # iterate through list
    for hit in hit_list:
        print("Collided!")

    # if pygame.sprite.collide_rect(Albertata, kai):
    #     print("You Suck")

    clock.tick(60)