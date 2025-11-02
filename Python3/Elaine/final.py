# "Magic Recipe Book"

# Pygame shows 3-5 ingredient buttons with pictures
# Click ingredients to select them
# Press "Create Recipe" button
# AI generates a silly recipe name + short description
# Display the result in a fun text box with animations
# That's it! Super simple loop


# write the name of each picture or like ingeredient on top of where it is showing
# have the ingredients  be organized in a grid so its easier to see them all

import pygame
# 1
from openai import OpenAI

# 2


# class Text to show above the ingredients

class Text:
    def __init__(self, surface, text, size, color, x, y):
        font_name = pygame.font.match_font('Poppins')
        self.surface = surface
        self.text = text
        self.size = size
        self.font = pygame.font.Font(font_name, self.size)
        self.color = color
        self.x = x
        self.y = y
    def draw(self):
        text_surface = self.font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (self.x, self.y)
        self.surface.blit(text_surface, text_rect)




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
pesto_img = pygame.image.load("pesto.png")
asparagus_img = pygame.image.load("asparagus.png")
banana_img = pygame.image.load("banana.png")
chimkins_img = pygame.image.load("chimkins.png")
cream_cheese_img = pygame.image.load("cream_cheese.png")
crepes_img = pygame.image.load("crepes.png")
fish_img = pygame.image.load("fish.png")
mus_turd_img = pygame.image.load("mus-turd.png")
mushrooms_img = pygame.image.load("mushrooms.png")
noods_img = pygame.image.load("noods.png")
pineapple_img = pygame.image.load("pineapple.png")
tomatoes_img = pygame.image.load("tomatoes.png")
# TODO: Load in the oil image here
# oil_img = pygame.image.load("oil.png")

potato_btn = Button(potato_img, 0.3, 40, 20)
potato_text = Text(screen, "Potato", 25, ( 255, 255, 255), 40, 70)

pesto_btn = Button(pesto_img, 0.2, 140, 20)
pesto_text = Text(screen, "Pesto", 25, (255, 255, 255), 140, 70)

asparagus_btn = Button(asparagus_img, 0.2, 240, 20)
asparagus_text = Text(screen, "Asparagus", 25, (255, 255, 255), 240, 70)

banana_btn = Button(banana_img, 0.3, 360, 20)
banana_text = Text(screen, "Banana", 25, (255, 255, 255), 360, 70)

cream_cheese_btn = Button(cream_cheese_img, 0.2, 40, 150)
cream_cheese_text = Text(screen, "Cream Cheese", 25, (255, 255, 255), 40, 205)

crepes_btn = Button(crepes_img, 0.2, 140, 150)
crepes_text = Text(screen, "Crepes", 25, (255, 255, 255), 140, 205)

fish_btn = Button(fish_img, 0.2, 240, 150)
fish_text = Text(screen, "Fish", 25, (255, 255, 255), 240, 205)

mus_turd_btn = Button(mus_turd_img, 0.2, 340, 150)
mus_turd_text = Text(screen, "Mustard", 25, (255, 255, 255), 340, 205)

mushrooms_btn = Button(mushrooms_img, 0.2, 440, 150)
mushrooms_text = Text(screen, "Mushrooms", 25, (255, 255, 255), 440, 205)

noods_btn = Button(noods_img, 0.2, 40, 310)
noods_text = Text(screen, "Noodles", 25, (255, 255, 255), 40, 365)

pineapple_btn = Button(pineapple_img, 0.4, 140, 310)
pineapple_text = Text(screen, "Pineapple", 25, (255, 255, 255), 140, 365)

tomatoes_btn = Button(tomatoes_img, 0.2, 240, 310)
tomatoes_text = Text(screen, "Tomatoes", 25, (255, 255, 255), 240, 365)

chimkins_btn = Button(chimkins_img, 0.2, 340, 310)
chimkins_text = Text(screen, "Chicken", 25, (255, 255, 255), 340, 365)
# TODO: Add the oil button here and the text 

# submit button

submit_img = pygame.image.load("subscribe.png")
submit_btn = Button(submit_img, 0.1, 350, 450)
foods = []

# Creating the texts to show above the ingredients

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()

      
  pygame.display.update() 
  screen.fill((0, 0, 0))
  # Check if buttons are clicked
  potato_text.draw()
  pesto_text.draw()
  asparagus_text.draw()
  banana_text.draw()
  cream_cheese_text.draw()
  crepes_text.draw()
  fish_text.draw()
  mus_turd_text.draw()
  mushrooms_text.draw()
  noods_text.draw()
  pineapple_text.draw()
  tomatoes_text.draw()
  chimkins_text.draw()
  # draw the oil test here 



  if potato_btn.draw():
    print("Potato")
    foods.append("potato")
  if pesto_btn.draw():
    print("Pesto")
    foods.append("pesto")
  if asparagus_btn.draw():
    print("Asparagus")
    foods.append("asparagus")
  if banana_btn.draw():
    print("Banana")
    foods.append("banana")
  if chimkins_btn.draw():
    print("Chicken")
    foods.append("chicken")
  if cream_cheese_btn.draw():
    print("Cream Cheese")
    foods.append("cream cheese")
  if crepes_btn.draw():
    print("Crepes")
    foods.append("crepes")
  if fish_btn.draw():
    print("Fish")
    foods.append("fish")
  if mus_turd_btn.draw():
    print("Mustard")
    foods.append("mustard")
  if mushrooms_btn.draw():
    print("Mushrooms")
    foods.append("mushrooms")
  if noods_btn.draw():
    print("Noodles")
    foods.append("noodles")
  if pineapple_btn.draw():
    print("Pineapple")
    foods.append("pineapple")
  if tomatoes_btn.draw():
    print("Tomatoes")
    foods.append("tomatoes")
  # TODO: Add the oil button draw check here -> if the button is clicked, print "Oil" and add "oil" to foods list

  # 3
  if submit_btn.draw():
    user_prompt = f"We want to bake a food with these ingredients.{foods}  give us sugestions of all the foods we can be making with detailed description of how to make it NOW! Make all of the dished be originated from france and be fancy and gourmet. Make fancy names for the dished and make sure they are unique and uncommen. You can give a whole meal with a dessert and appetizer. "

  # 4
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": user_prompt}
        ]
    )

  # 5
    print(response.choices[0].message.content)

  clock.tick(60)