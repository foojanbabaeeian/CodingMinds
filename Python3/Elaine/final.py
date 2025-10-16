# "Magic Recipe Book"

# Pygame shows 3-5 ingredient buttons with pictures
# Click ingredients to select them
# Press "Create Recipe" button
# AI generates a silly recipe name + short description
# Display the result in a fun text box with animations
# That's it! Super simple loop

import pygame
# 1
from openai import OpenAI

# 2
client = OpenAI(
    api_key = "<YOUR_API_KEY> "
)



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

potato_btn = Button(potato_img, 0.5, 0, 100)
pesto_btn = Button(pesto_img, 0.4, 0, 200)
asparagus_btn = Button(asparagus_img, 0.4, 100, 150)
banana_btn = Button(banana_img, 0.4, 100, 200)
chimkins_btn = Button(chimkins_img, 0.4, 200, 50)
cream_cheese_btn = Button(cream_cheese_img, 0.4, 200, 100)
crepes_btn = Button(crepes_img, 0.4, 150, 250)
fish_btn = Button(fish_img, 0.4, 150, 250)
mus_turd_btn = Button(mus_turd_img, 0.4, 150, 250)
mushrooms_btn = Button(mushrooms_img, 0.4, 150, 250)
noods_btn = Button(noods_img, 0.4, 150, 250)
pineapple_btn = Button(pineapple_img, 0.4, 150, 250)
tomatoes_btn = Button(tomatoes_img, 0.4, 150, 250)
# submit button
submit_img = pygame.image.load("subscribe.png")
submit_btn = Button(submit_img, 0.4, 350, 400)
foods = []
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
  

    # 3
  if submit_btn.draw():
    user_prompt = f"We want to bake a food with these ingredients.{foods}  give us sugestions of all the foods we can be making with detailed description of how to make it NOW!"

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