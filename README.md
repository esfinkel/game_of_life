# Game of Life
Based on the titular mathematical Gedankenexperiment by John Horton Conway.

From [the wikipedia page](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life):

  > The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, alive or dead, (or populated and unpopulated, respectively). Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:
  > - Any live cell with fewer than two live neighbors dies, as if by underpopulation.
  > - Any live cell with two or three live neighbors lives on to the next generation.
  > - Any live cell with more than three live neighbors dies, as if by overpopulation.
  > - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
  >
  > The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed; births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick. Each generation is a pure function of the preceding one. The rules continue to be applied repeatedly to create further generations.

Run the program in terminal; click on a square to "flip" it between states (blue is alive, red is dead). Press button on right side to pause/resume.

### Current issue 

Unfortunately, (some?) Macs do not support button background-coloring; on my computer, it's supported only when the widget is out-of-focus (using `highlightbackground`). Hence the button text.

https://stackoverflow.com/questions/1529847/how-to-change-the-foreground-or-background-colour-of-a-tkinter-button-on-mac-os 

~~NOTE: The .py file uses the package tkinter, which is currently buggy. In fact, the tkinter functions that the game uses crash my computer. Attempting to run this program is not advised at present.~~ It's working fine as of Feb 2020.