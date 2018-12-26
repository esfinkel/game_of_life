import numpy as np
import copy
from time import sleep
import tkinter as tk

def findnbs(row,col,reader):
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
        if self.g[r][c]==0:
            self.g[r][c]=1
        else:
            self.g[r][c]=0
        Game.set(self.buttons[r][c],{'text':Game.text(self.g[r][c]), 'highlightbackground':Game.color(self.g[r][c])})
        
    def set(button,fields):
        # fields could be {'text': 'ee', 'highlightbackground': 'red'}
        if 'text' in fields:
            button.configure(text = fields['text']);
        if 'highlightbackground' in fields:
            button.configure(highlightbackground = fields['highlightbackground']);
        return
    
    def text(s):
        return ''
    
    def color(i):
        cls = {0: 'red', 1: 'blue'}
        return cls[i]
    
    def pp(self):
        self.play = not self.play
            
    def draw(self):
        game = self.g
        pp = tk.Button(self.root, command=(lambda self=self: self.pp()), text='p')
        for r in range(len(game)):
            for c in range(len(game[0])):
                but = tk.Button(self.root, command = (lambda r=r, c=c: self.flip(r,c)))
                #but.bind('<Enter>', (lambda r=r, c=c: self.flip(r,c)))
                Game.set(but,{'text':Game.text(game[r][c]), 'highlightbackground':Game.color(game[r][c])})
                self.buttons[r][c] = but
                but.grid(row=r,column=c)
        pp.grid(row=0,column=len(game))

    def iterate(self):
        if not self.play:
            return
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
    
    def update(self):
        self.iterate()
        self.root.after(400, self.update) # run this function again in 400 milliseconds
        
def run_sample():
    g1 = make_sample_game(10)
    sleep(1)
    iterate(g1)
    sleep(1)
    iterate(g1)
    sleep(1)
    iterate(g1)
    sleep(1)
    iterate(g1)
    sleep(1)
    iterate(g1)
    sleep(1)
    iterate(g1)
    sleep(1)

if __name__ == '__main__':
    g = Game()
    g.draw()
    g.update()
    g.root.mainloop()