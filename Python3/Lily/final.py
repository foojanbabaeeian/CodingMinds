# Battleship 
# - coding function to spawn ships anywhere but no overlappping ships
# - shoot projecti;e to spot
# - shoot porjectile to X coordinate, Y coordinate. EX.  (5,8)
# - if projectile hit enemy ship say "HIT"
# - if not say "EMPTY" or "NOT HIT"
# - if sunk all enemy ships say "WIN"
# - if enemy sinks all your ships say "LOSE"
# - Computer vs Human or HUman vs human
# - function to make grid to put ships open


# Background: All blue        47, 91, 156
# When hit ship: yellow       237, 201, 52  
# When not hit ship: turn gray    93, 101, 105
# ships sunk: red         207, 23, 23  

Blue  = (47, 91, 156)
Gray  = (93, 101, 105)
Red   = (207, 23, 23)
Yellow= (237, 201, 52)

import pygame

class Button(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)

    self.rect = self.image.get_rect()
    self.rect.center = (x, y)
    self.clicked = False # include new variable 

  def draw(self):
    screen.blit(self.image, (self.rect.x, self.rect.y))
    pressed = False
    pos = pygame.mouse.get_pos()
    
    if self.rect.collidepoint(pos):
      if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
        self.clicked = True
        pressed = True
    if pygame.mouse.get_pressed()[0] == 0:
      self.clicked = False
    return pressed

pygame.init()
clock = pygame.time.Clock() # The clock tracks how fast the game is running.
screen_width, screen_height = 500, 500
screen = pygame.display.set_mode((screen_width, screen_height))


# buttons with just colors 
# ship parts are going to be blue 
# if hit we turn them to red and other parts ar just gray and if hit they turn to black

# ships are going to be 2, 3, 4 ships 


play_btn = Button(1, 150, 250)
pause_btn = Button(1, 350, 250)
# 10 by 10 square grid for the game buttons
grid = []
for row in range(10):
  grid.append([])
  for col in range(10):
    button = Button(1, col * 50, row * 50)
    grid[row].append(button)


while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()
      
  pygame.display.update() 
  screen.fill((0, 0, 0))

  if play_btn.draw():
    print("Play")
  if pause_btn.draw():
    print("Pause")

  clock.tick(60)


