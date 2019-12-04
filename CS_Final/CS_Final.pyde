import os
import random
path = os.getcwd()
NUM_DIM = 4
RESOLUTION = 800
Tile_Size = RESOLUTION/NUM_DIM
board=[]

class Tile():
    
    def __init__(self, r, c, number):
        self.r = r
        self.c = c
        self.number= number #intger
        # self.board= []
        
        # for r in range(NUM_DIM):
        #     smalllist=[]
        #     for c in range(NUM_DIM):
        #         smalllist.append(0)
        #     self.board.append(smalllist)
        
 
    def generate(self):
        pos=choice(self.vacancy)
        if randint(0,5)== 4:
            self.matrix[pos[0]][pos[1]] = 4
        else:
            self.matrix[pos[0]][pos[1]] = 2
        del self.vacancy[self.vacancy.index((pos[0], pos[1]))]
        
        
    def show(self):
        fill(120)
        stroke(255)
        rect(self.c * Tile_Size, self.r * Tile_Size, 200, 200)
    
    
        
class Puzzle(list):
    def __init__(self):
        for r in range(NUM_DIM):
            smalllist = []
            for c in range(NUM_DIM):
                smalllist.append(Tile(r, c, 0))
            self.append(smalllist)
        
    def show_tiles(self):
        # print(self)
        for tile in self:
            for i in tile:
                i.show()
                
        
            
        #stroke(255) #white 
        #background(126, 10, 203)  # NYU purple

puzzle = Puzzle()

def setup():
    # size(RESOLUTION, RESOLUTION)
    # background(0, 0, 0)
    size(RESOLUTION + Tile_Size , RESOLUTION)
   
def draw():
    background(255)
    # stroke (126, 10, 203)
    # strokeWeight(15)
    # rect(0, 0, RESOLUTION, RESOLUTION)
    puzzle.show_tiles()
    
    
