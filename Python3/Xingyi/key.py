import pygame

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((500, 500))

while True:
    screen.fill((0,0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keystate = pygame.key.get_pressed()
    
    #if up arrow, then draw a red box
    if keystate[pygame.K_UP]:
        rectangle = pygame.draw.rect(screen, (255, 0, 0), (390, 10, 100, 50))
    #if down arrow, then draw a green box
    elif keystate[pygame.K_DOWN]:
        rectangle = pygame.draw.rect(screen, (0, 255, 0), (100, 10, 50, 50))
    #if left arrow, then draw a blue box
    elif keystate[pygame.K_LEFT]:
        rectangle = pygame.draw.rect(screen, (0, 0, 255), (300, 200, 70, 50))
    #if right arrow, then draw a white box
    elif keystate[pygame.K_RIGHT]:
        rectangle = pygame.draw.rect(screen, (255, 255, 255), (250, 40, 45, 50))

    pygame.display.update()
    clock.tick(60)