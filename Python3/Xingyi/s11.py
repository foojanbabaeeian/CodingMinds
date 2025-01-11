import pygame
import random

class Player(pygame.sprite.Sprite):


  def __init__(self, image, scale, x, y):  
    pygame.sprite.Sprite.__init__(self)
    width = image.get_width()  
    height = image.get_height()
    #scale image by specified scale size
    self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)


  def update(self):
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_UP]:
      self.rect.y -= 7
    elif keystate[pygame.K_DOWN]:
      self.rect.y += 7
    elif keystate[pygame.K_LEFT]:
      self.rect.x -= 7
    elif keystate[pygame.K_RIGHT]:
      self.rect.x += 7


class Enemy(pygame.sprite.Sprite):
  def __init__(self, image,scale, x , y):
    pygame.sprite.Sprite.__init__(self)
    width = image.get_width()  
    height = image.get_height()
    #scale image by specified scale size
    self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
    self.rect = self.image.get_rect()
    self.rect.center = (random.randint(0,500), random.randint(0,500))
    self.speed = 1


  def update(self,target):
    # self.rect.x += random.choice ([0,-self.speed,self.speed])
    # self.rect.y += random.choice ([0,-self.speed,self.speed])
    # print("rfgydbmx")
    if self.rect.x > target.rect.x:
        self.rect.x-=self.speed


    if self.rect.x < target.rect.x:
        self.rect.x+=self.speed


    if self.rect.y > target.rect.y:
      self.rect.y-=self.speed


    if self.rect.y < target.rect.y:
      self.rect.y+=self.speed


def draw_text(color, text, font, size, x, y, surface):
    font_name = pygame.font.match_font(font)
    Font = pygame.font.Font(font_name, size)
    text_surface = Font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x,y)
    surface.blit(text_surface,text_rect)


pygame.init()
clock = pygame.time.Clock() # The clock tracks how fast the game is running.
screen_width, screen_height = 500, 500
screen = pygame.display.set_mode((screen_width, screen_height))


hamster_img = pygame.image.load("player.jpg")
player = Player(hamster_img, 0.12, 200, 200)
player_group = pygame.sprite.Group()
player_group.add(player)  # add player object to player group


cat_img = pygame.image.load("cat cute.jpg")
enemy = Enemy(cat_img, 0.6, 0, 0)
enemy_group = pygame.sprite.Group()
enemy_group.add(enemy)  

# GAME_FONT = pygame.freetype.Font("Comic Sans MS", 24)
def text_to_screen(screen, text, x, y, size = 50,
            color = (255, 255, 255), font_type = 'happy.ttf'):
    try:

        text = str(text)
        font = pygame.font.Font(font_type, size)
        text = font.render(text, True, color)
        screen.blit(text, (x, y))

    except Exception:
        print ('Font Error, saw it coming')

while True:
  score = 1
  # pygame.display.set_caption(f" Score: {score}")
  text_to_screen(screen, 'Score {}'.format(score), 10, 10)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()
     
  pygame.display.update()
  screen.fill((0, 0, 0))
  player_group.draw(screen)
  player_group.update() # update the sprite
  enemy_group.draw(screen)
  enemy_group.update(player)
  clock.tick(60)

