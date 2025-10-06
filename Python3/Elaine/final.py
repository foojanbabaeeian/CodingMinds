# "Magic Recipe Book"

# Pygame shows 3-5 ingredient buttons with pictures
# Click ingredients to select them
# Press "Create Recipe" button
# AI generates a silly recipe name + short description
# Display the result in a fun text box with animations
# That's it! Super simple loop

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

#HEIRLOOM TOMATO HAS NO END, Pineapple, Strawberry, Asparagus, Brussel Sprout, Salmon, Blueberry, Potato, Cream cheese, pesto sauce, Pasta, Chicken, Banana, Mustard, 
# ALL HAIL HEIRLOOM TOMATO tehehe

# 1, Find the images and load them in your python code
# 2, Create button instances for each image
# 3, Display the buttons on the screen

potato_img = pygame.image.load("potato.jpg")
blueberry_img = pygame.image.load("blueberry.jpg")

potato_btn = Button(potato_img, 1, 150, 250)
blueberry_btn = Button(blueberry_img, 1, 350, 250)


while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()

      
  pygame.display.update() 
  screen.fill((0, 0, 0))
  # Check if buttons are clicked

  if potato_btn.draw():
    print("Potato")
  if blueberry_btn.draw():
    print("Blueberry")

  clock.tick(60)