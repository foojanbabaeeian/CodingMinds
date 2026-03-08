import pygame

pygame.init()
clock = pygame.time.Clock() # The clock tracks how fast the game is running.
screen = pygame.display.set_mode((500, 500))

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()
                                        #R,   G,   B      X,  Y,  W,  H
  white_square = pygame.draw.rect(screen, (255, 255, 255), (10, 10, 50, 50))# surface, color, rect dimensions	
  brown_square = pygame.draw.rect(screen, (150, 75, 0), (60, 60, 200, 100))
  pygame.display.update()
  clock.tick(60)