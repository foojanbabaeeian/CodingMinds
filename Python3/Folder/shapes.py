import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))

white_square = pygame.draw.rect(screen, (255, 255, 255), (10, 10, 50, 50))# surface, color, rect dimensions	

rectangle = pygame.draw.rect(screen, (255, 0, 0), (390, 10, 100, 50))
                                    
circle = pygame.draw.circle(screen, (0, 255, 0), (200, 200), 25)
pink_pentagon = pygame.draw.polygon(screen, (255, 0, 230), [(146, 300), (272, 370), (236, 495), (56, 495), (20, 370)])
yellow_triangle = pygame.draw.polygon(screen, (248, 252, 3), [(10, 300), (40, 200), (70, 300) ]) # surface, color, list of points
white_square = pygame.draw.rect(screen, (255, 255, 255), (10, 10, 50, 50))
teal_square = pygame.draw.rect(screen, (0, 255, 255), (10, 10, 30, 30))