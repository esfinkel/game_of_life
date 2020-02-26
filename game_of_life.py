import numpy as np
import copy
from time import sleep
import tkinter as tk

# unfortunately (some?) Macs do not support button background-coloring
# https://stackoverflow.com/questions/1529847/how-to-change-the-foreground-or-background-colour-of-a-tkinter-button-on-mac-os 

def findnbs(row,col,reader):
    '''given cell, return number of neighbors'''
    total = 0
    positions = [[row-1,col-1],[row,col-1],[row+1,col-1],[row-1,col],[row+1,col],[row-1,col+1],[row,col+1],[row+1,col+1]]
    def fix(i):
        if i<0:
            return 'out-of-range'
        return i
    for pos in positions:
        pos = [fix(pos[0]),fix(pos[1])]
        #print([pos[0],pos[1]])
        try:
            total += reader[pos[0]][pos[1]]
            #print(reader[pos[0]][pos[1]])
        except:
            total += 0
    return total

def rule(neighbors,alive):
    '''return value of: cell should be alive'''
    if neighbors < 2:
        return 0
    if neighbors > 3:
        return 0
    if not alive and neighbors != 3:
        return 0
    return 1

def make_blank_game(n):
    game = [[0 for i in range(n)] for i in range(n)]
    return game

def make_sample_game(n):
    '''
    Makes game:
    ----------
    ----------
    ----------
    ----------
    -----O-O--
    ----OOOO--
    ----------
    ----------
    ----------
    ----------
    '''
    assert n>8
    template = make_blank_game(n)
    template[5][5] = 1
    template[5][6] = 1
    template[5][4] = 1
    template[5][7] = 1
    template[4][7] = 1
    template[4][5] = 1
    #printgame(template)
    return template

class Game:

    def __init__(self):
        self.g = make_sample_game(10)
        self.root = tk.Tk()
        self.play = True
        self.buttons = [[0 for i in range(len(self.g))] for j in range(len(self.g))]

    def flip(self,r,c):
        '''flip a cell'''
        if self.g[r][c]==0:
            self.g[r][c]=1
        else:
            self.g[r][c]=0
        Game.set(self.buttons[r][c],{'text':Game.text(self.g[r][c]), 'highlightbackground':Game.color(self.g[r][c])})

    @staticmethod
    def set(button, fields):
        '''set button properties'''
        # fields could be {'text': 'ee', 'highlightbackground': 'red'}
        if 'text' in fields:
            button.configure(text = fields['text'])
        if 'highlightbackground' in fields:
            button.configure(highlightbackground = fields['highlightbackground'], bg=fields['highlightbackground'])
            button.configure(fg = fields['highlightbackground'])
        return

    @staticmethod
    def text(s):
        '''return button text as a function of cell life'''
        return '###\n###\n###'

    @staticmethod
    def color(i):
        '''# return button color as a function of cell life'''
        cls = {0: 'red', 1: 'blue'}
        return cls[i]

    def pp(self):
        '''pause or play'''
        self.play = not self.play

    def draw(self):
        '''create buttons'''
        game = self.g
        butsize = 3
        p_button = tk.Button(self.root, command=(lambda self=self: self.pp()), text='pause', height=butsize, width=butsize*2)
        for r in range(len(game)):
            for c in range(len(game[0])):
                but = tk.Button(self.root, command = (lambda r=r, c=c: self.flip(r,c)), height=butsize, width=butsize)
                #but.bind('<Enter>', (lambda r=r, c=c: self.flip(r,c)))
                Game.set(but,{'text':Game.text(game[r][c]), 'highlightbackground':Game.color(game[r][c])})
                self.buttons[r][c] = but
                but.grid(row=r,column=c)
        #p_button.configure(text = 'p')
        p_button.grid(row=0,column=len(game))
        self.p_button = p_button

    def iterate(self):
        '''if in play, apply rules to every button, and then flip accordingly'''
        if self.play:
            self.p_button.configure(highlightbackground='white', background='white', fg='black')
            game = self.g
            reader = copy.deepcopy(game)
            m = len(reader)
            n = len(reader[0])
            for row in range(m):
                for col in range(n):
                    neighbors = findnbs(row,col,reader)
                    alive = reader[row][col]
                    game[row][col] = rule(neighbors,alive)
                    Game.set(self.buttons[row][col],{'text':Game.text(game[row][col]), 'highlightbackground':Game.color(game[row][col])})
                    #self.buttons[row][col].configure(text = game[row][col])
        else:
            self.p_button.configure(highlightbackground='purple', background='purple', fg='DarkRed')

    def update(self):
        self.iterate()
        self.root.after(400, self.update) # run this function again in 400 milliseconds

def run_sample():
    g1 = make_sample_game(10)
    sleep(1)
    g1.iterate()
    sleep(1)
    g1.iterate()
    sleep(1)
    g1.iterate()
    sleep(1)
    g1.iterate()
    sleep(1)
    g1.iterate()
    sleep(1)
    g1.iterate()
    sleep(1)

if __name__ == '__main__':
    g = Game()
    g.draw()
    g.update()
    g.root.mainloop()
