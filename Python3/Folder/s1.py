print("arson is fun:)")
print("""⠀⠀⠀⢀⡠⠤⠖⢒⠂⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣀⠀⠀⠀⠀⠀⢠⠖⠁⠀⠀⠀⠀⠀⠀⠢⣥⣢⠀⠀⠀⠀⠀⣠⣤⠀
⢀⣟⣿⣦⠀⠀⠀⣰⡿⠿⠷⠶⣄⠀⠀⢠⠾⠟⠛⠛⢷⡀⠀⢀⡼⣿⣇⡇
⠈⠛⠛⠿⢕⡂⢴⠁⠀⠀⠀⢀⠈⠆⠠⣮⣴⢤⡀⣀⣸⣗⣶⡧⠒⠉⠉⠁
⠀⠀⠀⠀⠀⢹⠀⠀⠴⣺⣿⣿⠇⠀⠀⠛⡿⣽⣿⣽⠿⠛⢻⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡌⠀⠀⠈⠉⢩⠀⠀⠀⠀⠀⣸⣒⣄⠀⠀⠀⠀⠇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡇⠀⢀⡴⠖⠉⠛⠓⠲⠶⠾⠿⠿⠿⢏⡳⡀⠄⣾⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠃⠀⠞⠀⣀⣀⣀⣀⣀⣀⣀⣤⣤⣶⣿⣇⢧⠀⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡄⠀⠀⠀⠈⠫⢽⣽⣉⣹⣁⣧⣿⠟⣱⣿⣾⢀⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢃⠀⠀⠀⠀⠀⠀⠉⠙⠩⠤⠭⣶⣋⡟⢸⢁⣿⠏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠝⡇⣘⡾⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠢⣀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣷⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠠⠤⠤⠤⠤⠾⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀""")


# Question: why do we use classes? What are classes? Why class player 
# We use classes becasuse i can have many players 
from turtle import circle
import pygame
import time

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((500, 500))

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


while True:
    screen.fill((0,0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # outside game loop
    game_text = Text(screen, "Welcome", 100, (255, 255, 255), 250, 0)
    Oo_ee = Text(screen, "OO EE OO AA AA", 50, (255, 255, 255), 250, 10)
    ting_tang = Text(screen, "Ting Tang", 20, (255, 255, 255), 250, 25)
    walla_walla = Text(screen, "WALLA WALLA", 80, (255, 255, 255), 250, 40)
    bing = Text(screen, "BING", 90, (255, 255, 255), 250, 70)
    bang = Text(screen, "BANG", 100, (255, 255, 255), 250, 70)
    # inside game loop
    game_text.draw()
    # how to maake the text appear after another
    keystate = pygame.key.get_pressed()

    if keystate[pygame.K_l]:
        rectangle = pygame.draw.circle(screen, (5, 89, 56), (200, 200),25)
        print("lily")
        

    #if up arrow, Lily
    elif keystate[pygame.K_UP]:
        rectangle = pygame.draw.circle(screen, (5, 89, 56), (200, 200),25)
        print("o   O EEE ")
        Oo_ee.draw()
    #if down arrow, Elaine
    elif keystate[pygame.K_DOWN]:
        pentadecagon = pygame.draw.polygon(screen, (0, 255, 0), [(100, 10), (150, 10), (175, 50), (125, 100), (75, 100), (25, 50)], 0)
        ting_tang.draw()
    #if left arrow, Lily
    # I need the points to a perfect hexagon where each side is the same length
    elif keystate[pygame.K_LEFT]:
        hexagon = pygame.draw.polygon(screen, (102, 0, 0), [(240, 230), (260, 230), (270, 250), (260, 270), (240, 270), (230, 250)], 0)
        walla_walla.draw()
    #if right arrow, Elaine 
    elif keystate[pygame.K_RIGHT]:
        triacontagon = pygame.draw.polygon(screen, (255, 255, 255), [(250, 40), (295, 40), (270, 10), (280, 0), (250, 0), (240, 10), (215, 40), (200, 40)], 0)
        bing.draw()
    elif keystate[pygame.K_SPACE]:
        pink_pentagon = pygame.draw.polygon(screen, (255, 0, 230), [(146, 300), (272, 370), (236, 495), (56, 495), (20, 370)])
        bang.draw()  





    