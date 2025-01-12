



import pygame 
  
pygame.init() 
  
# CREATING CANVAS 
canvas = pygame.display.set_mode((500, 500)) 
  
# TITLE OF CANVAS 
pygame.display.set_caption("My Board") 
exit = False
  
while not exit: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
    pygame.display.update() 