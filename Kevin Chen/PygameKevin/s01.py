import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 67

# Colors (Neon Palette)
BLACK = (10, 10, 15)
WHITE = (240, 240, 240)
NEON_BLUE = (0, 255, 255)
NEON_PINK = (255, 20, 147)
NEON_GREEN = (57, 255, 20)
GRID_COLOR = (30, 30, 50)

# Setup Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("NEON AVOIDANCE")
clock = pygame.time.Clock()

# Fonts
font_main = pygame.font.SysFont("Arial", 32, bold=True)
font_small = pygame.font.SysFont("Arial", 20)

class Player:
    def __init__(self):
        self.width = 40
        self.height = 40
        self.x = SCREEN_WIDTH // 2 - self.width // 2
        self.y = SCREEN_HEIGHT - 80
        self.speed = 8
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, keys):
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.rect.left > 0:
            self.rect.x -= self.speed
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

    def draw(self, surface):
        # Draw a glowing neon triangle for the player
        points = [
            (self.rect.centerx, self.rect.top),
            (self.rect.left, self.rect.bottom),
            (self.rect.right, self.rect.bottom)
        ]
        pygame.draw.polygon(surface, NEON_BLUE, points)
        # Inner glow effect
        pygame.draw.polygon(surface, WHITE, points, 2)

class Obstacle:
    def __init__(self, speed_multiplier):
        self.width = random.randint(30, 80)
        self.height = 20
        self.x = random.randint(0, SCREEN_WIDTH - self.width)
        self.y = -self.height
        self.speed = random.uniform(4, 7) * speed_multiplier
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = NEON_PINK if random.random() > 0.5 else NEON_GREEN

    def update(self):
        self.rect.y += self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        # Add a small white border for "glow"
        pygame.draw.rect(surface, WHITE, self.rect, 1)

def draw_background():
    screen.fill(BLACK)
    # Draw scrolling grid effect
    for i in range(0, SCREEN_WIDTH, 50):
        pygame.draw.line(screen, GRID_COLOR, (i, 0), (i, SCREEN_HEIGHT))
    for i in range(0, SCREEN_HEIGHT, 50):
        pygame.draw.line(screen, GRID_COLOR, (0, i), (SCREEN_WIDTH, i))

def main_game():
    player = Player()
    obstacles = []
    score = 0
    level = 1
    spawn_timer = 0
    game_active = True
    high_score = 0

    while True:
        keys = pygame.key.get_pressed()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if not game_active and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Reset Game
                    return main_game()

        if game_active:
            # 1. Update State
            player.move(keys)
            
            # Difficulty scaling
            speed_mult = 1 + (score // 1000) * 0.2
            spawn_rate = max(10, 30 - (score // 500))

            # Spawn Obstacles
            spawn_timer += 1
            if spawn_timer > spawn_rate:
                obstacles.append(Obstacle(speed_mult))
                spawn_timer = 0

            # Move and filter obstacles
            for obs in obstacles[:]:
                obs.update()
                if obs.rect.top > SCREEN_HEIGHT:
                    obstacles.remove(obs)
                    score += 10
                
                # Collision Detection
                if player.rect.colliderect(obs.rect):
                    game_active = False

            # 2. Draw everything
            draw_background()
            
            for obs in obstacles:
                obs.draw(screen)
            
            player.draw(screen)

            # UI
            score_text = font_main.render(f"SCORE: {score}", True, WHITE)
            screen.blit(score_text, (20, 20))
            
        else:
            # Game Over Screen
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            screen.blit(overlay, (0, 0))

            msg = font_main.render("SYSTEM CRASHED", True, NEON_PINK)
            restart_msg = font_small.render("Press SPACE to Reboot", True, WHITE)
            final_score = font_main.render(f"FINAL SCORE: {score}", True, NEON_BLUE)
            
            screen.blit(msg, (SCREEN_WIDTH//2 - msg.get_width()//2, 200))
            screen.blit(final_score, (SCREEN_WIDTH//2 - final_score.get_width()//2, 260))
            screen.blit(restart_msg, (SCREEN_WIDTH//2 - restart_msg.get_width()//2, 350))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main_game()