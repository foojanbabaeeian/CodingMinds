import pygame
import random
pygame.init()

s_width = 400
s_height = 250

screen = pygame.display.set_mode((s_width, s_height))
clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)


class Player(pygame.sprite.Sprite):
  def __init__(self, image):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.transform.scale(image, (40,40))
    self.rect = self.image.get_rect()
    self.rect.bottomleft = (0, s_height)

  def update(self):
    #Movement Keybinds for Player Here
	
	

    #Prevents player from leaving boundary
    if self.rect.left <= 0:
      self.rect.left = 0
    if self.rect.bottom >= s_height:
      self.rect.bottom = s_height
    if self.rect.top <= 0:
      self.rect.top = 0
    if self.rect.right >= s_width:
      self.rect.right = s_width

class Enemy(pygame.sprite.Sprite):
  def __init__(self, image, x , y):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.transform.scale(image, (40,40))
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)
    self.speed = 1

  def update(self, target):
    if self.rect.x > target.rect.x:
      #Fill in code here

    if self.rect.y > target.rect.y:
      #Fill in code here

def draw_text(color, text, font, size, x, y, surface):
  font_name = pygame.font.match_font(font)
  Font = pygame.font.Font(font_name, size)
  text_surface = Font.render(text, True, color)
  text_rect = text_surface.get_rect()
  text_rect.center = (x,y)
  surface.blit(text_surface,text_rect)
  
    
    
#IMPORT IMAGES:
player_img = pygame.image.load('player_image.filetype')
enemy_img = pygame.image.load('enemy_image.filetype')


#CREATING SPRITE GROUPS:
allSprites = pygame.sprite.Group()
enemySprites = pygame.sprite.Group()

#CREATING OBJECTS:


#ADD OBJECTS TO GROUPS:


time = 0
reset = 0
game_state = "Play"
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()

  if game_state == "Lose":
    #BLIT GAMEOVER BACKGROUND TO SCREEN  
  else:
    screen.fill(white)
    
    #Collisions Here
   
  
    #TIMER FOR PLAYER:
    time = pygame.time.get_ticks()/1000
    #Draw Text for correct time:
    
    
    #TEN SECOND TIMER FOR ENEMY:
    milliseconds = pygame.time.get_ticks() - reset
    if milliseconds >= 10000:
      reset+= 10000
      enemy = Enemy(enemy_img, random.randint(0,s_width), random.randint(0,s_height))
      enemySprites.add(enemy)
    
    
    #DRAWING TO SCREEN:
    
  
    #UPDATE GROUPS:
    
  
    
  clock.tick(40)
  pygame.display.update()