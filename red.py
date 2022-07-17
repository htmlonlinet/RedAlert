import random
FONT_COLOR = (255, 255, 255)
WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X, CENTER_Y)
FINAL_LEVEL = 6
START_SPEED = 10
COLORS = ["green", "blue"]
game_over = False
current_level = 1
stars = []
animations = []
def draw():
  global stars, current_level, game_over, game_complete
  screen.clear()
  screen.blit("space", (0:0))
