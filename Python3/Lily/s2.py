import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((73, 73))

pygame.mixer.music.load("The Green Orbs.mp3")

pygame.mixer.music.play(1)

while True:
    screen.fill((0,0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
    clock.tick(60)

        



    
