import pygame

class Button(pygame.sprite.Sprite):
  def __init__(self, image, scale, x, y):
    pygame.sprite.Sprite.__init__(self)
    width = image.get_width()
    height = image.get_height()
    self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
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


play_img = pygame.image.load("playButton.png")
pause_img = pygame.image.load("pauseButton.png")

play_btn = Button(play_img, 1, 150, 250)
pause_btn = Button(pause_img, 1, 350, 250)


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