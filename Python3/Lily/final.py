# Battleship 
# - coding function to spawn ships anywhere but no overlappping ships
# - button to shoot projectile to a spot
# - shoot porjectile to X coordinate, Y coordinate. EX.  (5,8)
# - if projectile hit enemy ship square turn yellow
# - if not say then square turn gray
# - if sunk all enemy ships say "WIN"
# - if you use up all your bullets say "LOSE"
# - function to make grid to put ships open
# - button for each square

# Background: All blue        47, 91, 156
# When hit ship: yellow       237, 201, 52  
# When not hit ship: turn gray    93, 101, 105
# ships sunk: red         207, 23, 23  

# LEVEL IDEAS
# - less bullets 
#    - Round 1: 75 bullets
#    - Round 2: 50 bullets
#    - Round 3: 35 bullets
# - less/no hints
#    - Round 1: 2 hints
#    - Round 2: 1 hint
#    - Round 3: no hints
# - bigger grid/ocean
#    - Round 1: 5x5
#    - Round 2: 7x7
#    _ Round 3: 10x10

# We need to also show where the not found ships were with a different color


BLUE  = (47, 91, 156) # background
GRAY  = (93, 101, 105) # When hit water
RED   = (207, 23, 23) # ships sunk
YELLOW = (237, 201, 52) # hit ship
BLACK = (0,0,0) # text color "LOSE" 
WHITE = (255,255,255) # other text color 
GREEN = (47, 158, 90) # "WIN"
LIGHT_GRAY = (145, 145, 142) # unsunken ships reveal


import pygame
import random

class Button(pygame.sprite.Sprite):
  def __init__(self, color, x, y, width=40, height=40):
    pygame.sprite.Sprite.__init__(self)
    
    # Create colored rectangle for the button
    self.image = pygame.Surface((width, height))
    self.image.fill(color)
    self.color = color
    self.original_color = color
    
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.clicked = False
    
    # Game state for this cell
    self.state = "empty"  # "empty", "ship", "hit", "miss", "sunk"
    self.width = width
    self.height = height
    self.ship_id = None  # Track which ship this cell belongs to

  def draw(self, screen):
    screen.blit(self.image, (self.rect.x, self.rect.y))
    # Draw white border around each cell
    pygame.draw.rect(screen, WHITE, self.rect, 2)
    
    pressed = False
    pos = pygame.mouse.get_pos()
    
    if self.rect.collidepoint(pos):
      if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
        self.clicked = True
        pressed = True
    if pygame.mouse.get_pressed()[0] == 0:
      self.clicked = False
    return pressed
  
  def set_visual_color(self, color):
    """Change the visual color of the cell"""
    self.image = pygame.Surface((self.width, self.height))
    self.image.fill(color)
    self.color = color


def can_place_ship(grid, row, col, direction, length):
  """Check if ship can be placed without overlapping"""
  # Check bounds
  if direction == "horizontal":
    if col + length > len(grid[0]):
      return False
    # Check for overlap
    for c in range(col, col + length):
      if grid[row][c].state == "ship":
        return False
  else:  # vertical
    if row + length > len(grid):
      return False
    # Check for overlap
    for r in range(row, row + length):
      if grid[r][col].state == "ship":
        return False
  
  return True


def place_ship(grid, row, col, direction, length, ship_id, hide_ships=True):
  """Place a ship on the grid"""
  coords = []
  
  if direction == "horizontal":
    for c in range(col, col + length):
      grid[row][c].state = "ship"  # Store that there's a ship here
      grid[row][c].ship_id = ship_id  # Track which ship this belongs to
      if not hide_ships:
        # Show ships during setup/debug (optional)
        grid[row][c].set_visual_color(YELLOW)
      coords.append((row, c))
  else:  # vertical
    for r in range(row, row + length):
      grid[r][col].state = "ship"
      grid[r][col].ship_id = ship_id
      if not hide_ships:
        # Show ships during setup/debug (optional)
        grid[r][col].set_visual_color(YELLOW)
      coords.append((r, col))
  
  return coords


def place_ships_randomly(grid, num_ships=3, hide_ships=True):
  """Place ships randomly on the grid"""
  ships_placed = 0
  ship_positions = []
  length_ships = [2, 3, 4]


  for ship_length in length_ships:
    # Random starting position
    row = random.randint(0, len(grid) - 1)
    col = random.randint(0, len(grid[0]) - 1)
    
    # Random direction and length
    direction = random.choice(["horizontal", "vertical"])
    
    
    # Try to place ship
    if can_place_ship(grid, row, col, direction, ship_length):
      ship_coords = place_ship(grid, row, col, direction, ship_length, ships_placed, hide_ships)
      ship_positions.append({
        'id': ships_placed,
        'coords': ship_coords,
        'sunk': False
      })
      ships_placed += 1
  
  return ship_positions


def check_ship_sunk(grid, ship_positions, row, col):
  """Check if the entire ship at this position is sunk"""
  # Find which ship was hit
  for ship in ship_positions:
    if (row, col) in ship['coords']:
      # Check if all parts of this ship are hit
      all_hit = True
      for r, c in ship['coords']:
        if grid[r][c].state != "hit":
          all_hit = False
          break
      
      if all_hit and not ship['sunk']:
        # Mark ship as sunk
        ship['sunk'] = True
        # Turn all parts RED
        for r, c in ship['coords']:
          grid[r][c].state = "sunk"
          grid[r][c].set_visual_color(RED)
        return True
  
  return False


def check_game_over(ships_sunk, total_ships, bullets_left):
  """Check if game is won or lost"""
  if ships_sunk == total_ships:
    return "WIN"
  elif bullets_left <= 0:
    return "LOSE"
  return "PLAYING"


def draw_ui(screen, bullets_left, ships_sunk, total_ships, game_status):
  """Draw game information"""
  font = pygame.font.Font(None, 32)
  
  # Title
  title = font.render("BATTLESHIP", True, WHITE)
  screen.blit(title, (200, 10))
  
  # Bullets
  bullets_text = font.render(f"Bullets: {bullets_left}", True, WHITE)
  screen.blit(bullets_text, (50, 520))
  
  # Ships
  ships_text = font.render(f"Ships Sunk: {ships_sunk}/{total_ships}", True, WHITE)
  screen.blit(ships_text, (270, 520))
  
  # Game Over Messages
  if game_status == "WIN":
    big_font = pygame.font.Font(None, 64)
    win_text = big_font.render("YOU WIN!", True, GREEN)
    screen.blit(win_text, (150, 250))
    
    small_font = pygame.font.Font(None, 28)
    restart_text = small_font.render("Press R to Restart", True, WHITE)
    screen.blit(restart_text, (165, 320))
    
  elif game_status == "LOSE":
    big_font = pygame.font.Font(None, 64)
    lose_text = big_font.render("YOU LOSE!", True, BLACK)
    screen.blit(lose_text, (140, 250))
    
    small_font = pygame.font.Font(None, 28)
    restart_text = small_font.render("Press R to Restart", True, WHITE)
    screen.blit(restart_text, (165, 320))


def draw_legend(screen):
  """Draw legend showing what colors mean"""
  font = pygame.font.Font(None, 22)
  x, y = 510, 80
  
  title_font = pygame.font.Font(None, 24)
  title = title_font.render("Legend:", True, WHITE)
  screen.blit(title, (x - 5, y - 30))
  
  # Water
  pygame.draw.rect(screen, BLUE, (x, y, 25, 25))
  pygame.draw.rect(screen, WHITE, (x, y, 25, 25), 2)
  text = font.render("Water", True, WHITE)
  screen.blit(text, (x + 30, y + 3))
  
  # Hit
  pygame.draw.rect(screen, YELLOW, (x, y + 35, 25, 25))
  pygame.draw.rect(screen, WHITE, (x, y + 35, 25, 25), 2)
  text = font.render("Hit", True, WHITE)
  screen.blit(text, (x + 30, y + 38))
  
  # Miss
  pygame.draw.rect(screen, GRAY, (x, y + 70, 25, 25))
  pygame.draw.rect(screen, WHITE, (x, y + 70, 25, 25), 2)
  text = font.render("Miss", True, WHITE)
  screen.blit(text, (x + 30, y + 73))
  
  # Sunk
  pygame.draw.rect(screen, RED, (x, y + 105, 25, 25))
  pygame.draw.rect(screen, WHITE, (x, y + 105, 25, 25), 2)
  text = font.render("Sunk", True, WHITE)
  screen.blit(text, (x + 30, y + 108))


def init_game():
  """Initialize/Reset the game"""
  # Create 10x10 grid
  GRID_SIZE = 10
  CELL_SIZE = 45
  GRID_OFFSET_X = 50
  GRID_OFFSET_Y = 60
  
  grid = []
  for row in range(GRID_SIZE):
    grid.append([])
    for col in range(GRID_SIZE):
      x = GRID_OFFSET_X + col * CELL_SIZE
      y = GRID_OFFSET_Y + row * CELL_SIZE
      button = Button(BLUE, x, y, CELL_SIZE, CELL_SIZE)
      button.state = "empty"
      grid[row].append(button)
  
  # Place ships (hide_ships=True means they stay blue, =False shows them)
  ship_positions = place_ships_randomly(grid, num_ships=3, hide_ships=True)
  
  # Game variables
  bullets_left = 60
  ships_sunk = 0
  total_ships = 3
  
  return grid, ship_positions, bullets_left, ships_sunk, total_ships


# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()
screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Battleship")

# Initialize game
grid, ship_positions, bullets_left, ships_sunk, total_ships = init_game()

# Game loop
running = True
game_status = "PLAYING"

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    
    # Restart game with R key
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_r:
        grid, ship_positions, bullets_left, ships_sunk, total_ships = init_game()
        game_status = "PLAYING"
        print("Game restarted!")
      
  screen.fill(BLACK)

  # Draw grid and handle clicks
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      cell = grid[row][col]
      
      # Only allow shooting if game is still playing
      if cell.draw(screen) and game_status == "PLAYING":
        
        if cell.state == "empty":
          # MISS - hit water, turn GRAY
          cell.state = "miss"
          cell.set_visual_color(GRAY)
          print(f"MISS at ({row}, {col})")
          bullets_left -= 1
          
        elif cell.state == "ship":
          # HIT - hit a ship, turn YELLOW
          cell.state = "hit"
          cell.set_visual_color(YELLOW)
          print(f"HIT at ({row}, {col})!")
          bullets_left -= 1
          
          # Check if ship is completely sunk
          if check_ship_sunk(grid, ship_positions, row, col):
            print("SHIP COMPLETELY SUNK! (Turned RED)")
            ships_sunk += 1
            
        elif cell.state == "hit" or cell.state == "miss" or cell.state == "sunk":
          # Already shot here
          print("Already shot here!")
      
      # If not playing, still draw but don't allow clicks
      elif game_status != "PLAYING":
        screen.blit(cell.image, (cell.rect.x, cell.rect.y))
        pygame.draw.rect(screen, WHITE, cell.rect, 2)
  
  # Check game over
  game_status = check_game_over(ships_sunk, total_ships, bullets_left)
  
  # Draw UI
  draw_ui(screen, bullets_left, ships_sunk, total_ships, game_status)
  draw_legend(screen)
  
  pygame.display.update() 
  clock.tick(60)

pygame.quit()