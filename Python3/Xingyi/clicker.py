import pygame
import time
from os import path 

pygame.init()

count = 0
screen_width = 500
screen_height = 280

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Candy Clicker")

black = (0, 0, 0)
turquoise = (138, 255, 239)

font_name = pygame.font.match_font('comic sans ms')
def draw_text(surf, text, size, x, y):
  font = pygame.font.Font(font_name, size)
  text_surface = font.render (text, True, black)
  text_rect = text_surface.get_rect()
  text_rect.midtop = (x, y)
  surf.blit(text_surface, text_rect)

#game loop 
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()
      
  # Assign the returned `get_pressed()` value to a variable
  
  # Complete the condition below to check if the space bar was pressed
  if :
      count += 1
      time.sleep(0.1)
  
  # Fill screen background with turquoise color here
  
  # Create circle candy here 
  
  draw_text(screen, "Candy: " + str(count), 30, screen_width/2, screen_height/20)
  pygame.display.update()