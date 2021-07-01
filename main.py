'''
CMPLXSY S11 Group 8 - Conway's Game of Life

Professor: Dr. Briane Paul Samson
Members:
BADULIS, Keith Gabriel N.
LUA, Matthew Walden B.
NILL, Byron Ethelbert V.
'''

from os import system, name
import random
from time import sleep

DEAD = ' '
LIVE = '○'
SURV = '•'
h = int(input('Enter the grid height (from 10 to 50): '))
while h not in range(10, 51):
    h = int(input('Invalid. Enter the grid height (from 10 to 50): '))
w = int(input('Enter the grid width (from 10 to 50): ')) 
while w not in range(10, 51):
    w = int(input('Invalid. Enter the grid width (from 10 to 50): '))
grid_size = (h, w)
n_iters = int(input('Enter the number of iterations: '))

class P:
  def __init__(self, x, y):
    self.x = x
    self.y = y

def clear_screen():
  if name == 'nt':
    system('cls')
  else:
    system('clear')

def print_grid(grid):
  for row in grid:
    for cell in row:
      print(cell, end='')
    print()

def count_living_neighbors(g, x, y):
  dx = [0, 1, 0, -1, 1, 1, -1, -1]  
  dy = [1, 0, -1, 0, 1, -1, -1, 1]
  ans = 0
  for i in range(8):
    new_x = x + dx[i]
    new_y = y + dy[i] 
    if new_x in range(0, grid_size[0]) and new_y in range(0, grid_size[1]):
      if g[new_x][new_y] == LIVE or g[new_x][new_y] == SURV:
        ans += 1
  return ans

# Updates the grid state from a set of rules
def update_state(grid):
  res = grid
  for i in range(grid_size[0]):
    for j in range(grid_size[1]):
      if grid[i][j] == SURV:
        grid[i][j] = LIVE
      c = count_living_neighbors(grid, i, j)
      if c == 3 and grid[i][j] == DEAD:
        res[i][j] = LIVE
      elif (c == 2 or c == 3) and (grid[i][j] == LIVE or grid[i][j] == SURV):
        res[i][j] = SURV
      else:
        res[i][j] = DEAD
  return res

def generate_clusters(x, y):
  dx = [0, 1, 0, -1, 1, 1, -1, -1]  
  dy = [1, 0, -1, 0, 1, -1, -1, 1]
  res = []
  # Pick up to 2 random neighboring cells to fill in
  for _ in range(2):
    i = random.randint(0, 7)
    new_x = x + dx[i]
    new_y = y + dy[i] 
    if new_x in range(0, grid_size[0]) and new_y in range(0, grid_size[1]):
      res.append(P(new_x, new_y))
  return res

# Initialize
grid = [[DEAD for _ in range(grid_size[1])] for i in range(grid_size[0])]
q0 = []
n = random.randint(3, grid_size[0] * grid_size[1] // 4)

# Place random initial live clusters around the grid
for i in range(n): # can modify this value or have the user define number of clusters
  x = random.randint(0, grid_size[0])
  y = random.randint(0, grid_size[1])
  q0.extend(generate_clusters(x, y))
for coords in q0:
  grid[coords.x][coords.y] = LIVE

# Run the program
for i in range(n_iters):
  clear_screen()
  print_grid(grid)
  grid = update_state(grid)
  sleep(0.2)
