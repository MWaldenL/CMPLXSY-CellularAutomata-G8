# Conway's Game of Life
This is a command-line implementation of Conway's Game of Life, written in Python 3, in fulfillment of the course, Complex Systems (CMPLXSY).

## Usage
1. Open a terminal or command-line interface.
2. Type `python3 main.py` or `python main.py`.
3. Enter the grid height, width, and number of iterations as prompted. 

## Rules
1. Initially, the grid is randomly populated with a minimum of three clusters and a maximum equal to the grid area divided by four.
2. Any surviving cell from the previous iteration will live.
3. The following rules shall apply following the Moore configuration:
- If a dead cell is surrounded by three live neighboors, the cell will live.
- If a live cell is surrounded by two or three live neighbors, the cell will survive.
- Otherwise, the cell will die.

## Members: 
CMPLXSY S11, ALT Group 8
1. Badulis, Keith Gabriel N.
2. Lua, Matthew Walden B.
3. Nill, Byron Ethelbert V.
