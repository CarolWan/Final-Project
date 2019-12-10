import os
import random
from time import sleep
path = os.getcwd()
size_game = 1000
n1 = 0
done = False

n3 = 250

loc_list = []


num_dim1 = 4
size_tile1 = 100
bold_edge1 = 6

board = [[0]*num_dim1 for i in range(num_dim1)]

size_edge1 = size_tile1/bold_edge1


# gamefont = createFont(path+'/ClearSans-Bold.ttf', 50)
# gamefont = createFont('/Users/NYUAD/Desktop/game2048/ClearSans-Bold.ttf', 50)

def settings():
    size(size_game, size_game)
    
def setup():
    global gamefont
    global gamefont2
    global gamefont3
    gamefont = createFont(path+'/ClearSans-Bold.ttf', 50)
    gamefont2 = createFont(path+'/ClearSans-Bold.ttf', 43)
    gamefont3 = createFont(path+'/ClearSans-Bold.ttf', 34)
    background(250,248,240)
    g.display_board()
    g.generate_first_tiles()
    g.display_board()
    print(path)

def draw():
    global done
    g.display_board()
    if keyPressed == True and done == True:
        g.generate_tile()
        done = False
        


        

class Game:
    
    def __init__(self, num_dim, size_tile, bold_edge):
        self.num_dim = num_dim
        self.size_tile = size_tile
        self.bold_edge = bold_edge
        self.size_edge = 100/self.bold_edge
        self.size_board = self.size_edge+(self.size_edge+self.size_tile)*self.num_dim
        
    def display_board(self):
        global n3
        global gamefont
        global gamefont2
        global gamefont3
        noStroke()
        fill(187,173,161)
        rect(n3, n3, self.size_board, self.size_board, 10)
        for i in range(4):
            for j in range(4):
                if board[i][j] == 0:
                    noStroke()
                    fill(205,193,181)
                    rect(n3+self.size_edge+(self.size_edge+self.size_tile)*j, n3+self.size_edge+(self.size_edge+self.size_tile)*i, self.size_tile, self.size_tile, 5)
                elif board[i][j] == 2:
                    fill(237,226,234) #(222,224,234) #(238,228,219)
                    rect(n3+self.size_edge+(self.size_edge+self.size_tile)*j, n3+self.size_edge+(self.size_edge+self.size_tile)*i, self.size_tile, self.size_tile, 5)
                elif board[i][j] == 4:
                    fill(202,169,193) #(229,218,227)#(237,224,203)
                    rect(n3+self.size_edge+(self.size_edge+self.size_tile)*j, n3+self.size_edge+(self.size_edge+self.size_tile)*i, self.size_tile, self.size_tile, 5)
                elif board[i][j] == 8:
                    fill(174,123,169) #(216,191,216) #(255,182,193)#(242,176,129)
                    rect(n3+self.size_edge+(self.size_edge+self.size_tile)*j, n3+self.size_edge+(self.size_edge+self.size_tile)*i, self.size_tile, self.size_tile, 5)
                elif board[i][j] == 16:
                    fill(147,90,132) #(219,112,147)#(245,148,107)
                    rect(n3+self.size_edge+(self.size_edge+self.size_tile)*j, n3+self.size_edge+(self.size_edge+self.size_tile)*i, self.size_tile, self.size_tile, 5)
                elif board[i][j] == 32:
                    fill(118,72,106) #(218,112,214)#(247,124,101)
                    rect(n3+self.size_edge+(self.size_edge+self.size_tile)*j, n3+self.size_edge+(self.size_edge+self.size_tile)*i, self.size_tile, self.size_tile, 5)
                elif board[i][j] == 64:
                    fill(94,58,85)#(238,130,238)#(247,93,69)
                    rect(n3+self.size_edge+(self.size_edge+self.size_tile)*j, n3+self.size_edge+(self.size_edge+self.size_tile)*i, self.size_tile, self.size_tile, 5)
                elif board[i][j] == 128:
                    fill(192,165,187)#(237,207,128)
                    rect(n3+self.size_edge+(self.size_edge+self.size_tile)*j, n3+self.size_edge+(self.size_edge+self.size_tile)*i, self.size_tile, self.size_tile, 5)
                elif board[i][j] == 256:
                    fill(87,6,140) #(237,204,110)
                    rect(n3+self.size_edge+(self.size_edge+self.size_tile)*j, n3+self.size_edge+(self.size_edge+self.size_tile)*i, self.size_tile, self.size_tile, 5)
                elif board[i][j] == 512:
                    fill(128,0,128)#(237,200,97)
                    rect(n3+self.size_edge+(self.size_edge+self.size_tile)*j, n3+self.size_edge+(self.size_edge+self.size_tile)*i, self.size_tile, self.size_tile, 5)
                elif board[i][j] == 1024:
                    fill(102,0,102)
                    rect(n3+self.size_edge+(self.size_edge+self.size_tile)*j, n3+self.size_edge+(self.size_edge+self.size_tile)*i, self.size_tile, self.size_tile, 5)
                elif board[i][j] == 2048:
                    fill(82,0,82)#(195,139,71)
                    rect(n3+self.size_edge+(self.size_edge+self.size_tile)*j, n3+self.size_edge+(self.size_edge+self.size_tile)*i, self.size_tile, self.size_tile, 5)
                    
                if board[i][j] == 2 or board[i][j] == 4:
                    textFont(gamefont)
                    fill(119,110,102)
                    text(str(board[i][j]), n3+self.size_edge+(self.size_edge+self.size_tile)*j+35, n3+self.size_edge+(self.size_edge+self.size_tile)*i+65)
                elif board[i][j] != 0:
                    if len(str(board[i][j])) == 1:
                        textFont(gamefont)
                        fill(249,246,242)
                        text(str(board[i][j]), n3+self.size_edge+(self.size_edge+self.size_tile)*j+35, n3+self.size_edge+(self.size_edge+self.size_tile)*i+65)
                    elif len(str(board[i][j])) == 2:
                        textFont(gamefont)
                        fill(249,246,242)
                        text(str(board[i][j]), n3+self.size_edge+(self.size_edge+self.size_tile)*j+20, n3+self.size_edge+(self.size_edge+self.size_tile)*i+65)
                    elif len(str(board[i][j])) == 3:
                        textFont(gamefont2)
                        fill(249,246,242)
                        text(str(board[i][j]), n3+self.size_edge+(self.size_edge+self.size_tile)*j+10, n3+self.size_edge+(self.size_edge+self.size_tile)*i+65)
                    elif len(str(board[i][j])) == 4:
                        textFont(gamefont3)
                        fill(249,246,242)
                        text(str(board[i][j]), n3+self.size_edge+(self.size_edge+self.size_tile)*j+10, n3+self.size_edge+(self.size_edge+self.size_tile)*i+62)
                           
            
    def generate_first_tiles(self):
        
        global board
        global loc_list
        global n1
        for i in range(2):
            for i in range(num_dim1):
                for j in range(num_dim1):
                    if board[i][j] == 0:
                        loc_list.append((i,j))
            v1 = random.choice([2,4])
            loc1 = random.choice(loc_list)
            r1 = loc1[0]
            c1 = loc1[1]
            board[r1][c1] = v1
            del loc_list[:]
        
       
    def generate_tile(self):
        
        global board
        global loc_list
        global n1
        for i in range(num_dim1):
            for j in range(num_dim1):
                if board[i][j] == 0:
                    loc_list.append((i,j))
        v1 = random.choice([2,4])
        loc1 = random.choice(loc_list)
        r1 = loc1[0]
        c1 = loc1[1]
        board[r1][c1] = v1
        del loc_list[:]
    
                                     
g = Game(num_dim1, size_tile1, bold_edge1) 


def move_down():
    
    global board
    global down_start
    for col in range(num_dim1):
        for row in range(num_dim1-1, -1, -1):
            if board[row][col] > 0:
                v2 = board[row][col]
                for i in range(1,4):
                    if row+i < num_dim1:
                        if board[row+i][col] == 0:
                            board[row+i-1][col] = 0
                            board[row+i][col] = v2
                            g.display_board()
                        # elif board[row+i][col] == v2:
                        #     board[row+i][col] = 2*v2
                        #     board[row+i-1][col] = 0
                        #     g.display_board()
   
        
        
def merge_down():
    
    for i in range(num_dim1):
        for j in range(num_dim1-1, 0, -1):
            a = board[j][i]
            b = board[j-1][i]
            if a == b:
                board[j][i] = a+b
                board[j-1][i] = 0
                
def merge_up():
    
    for i in range(num_dim1):
        for j in range(0, num_dim1-1):
            a = board[j][i]
            b = board[j+1][i]
            if a == b:
                board[j][i] = a+b
                board[j+1][i] = 0
                
def merge_left():
    
    for i in range(num_dim1):
        for j in range(0, num_dim1-1):
            a = board[i][j]
            b = board[i][j+1]
            if a == b:
                board[i][j+1] = a+b
                board[i][j] = 0
                
def merge_right():
    
    for i in range(num_dim1):
        for j in range(num_dim1-1, 0, -1):
            a = board[i][j]
            b = board[i][j-1]
            if a == b:
                board[i][j-1] = a+b
                board[i][j] = 0
        
def move_up():
    
    global board
    global up_start
    for col in range(num_dim1):
        for row in range(num_dim1):
            if board[row][col] > 0:
                v2 = board[row][col]
                for i in range(1,4):
                    if row-i > -1:
                        if board[row-i][col] == 0:
                            board[row-i+1][col] = 0
                            board[row-i][col] = v2
                            g.display_board()
                        # elif board[row-i][col] == v2:
                        #     board[row-i][col] = 2*v2
                        #     board[row-i+1][col] = 0
                        #     g.display_board()
        
        
def move_left():
    
    global board
    global left_start
    for row in range(num_dim1):
        for col in range(num_dim1):
            if board[row][col] > 0:
                v2 = board[row][col]
                for i in range(1,4):
                    if col-i > -1:
                        if board[row][col-i] == 0:
                            board[row][col-i+1] = 0
                            board[row][col-i] = v2
                            g.display_board()
                        # elif board[row][col-i] == v2:
                        #     board[row][col-i] = 2*v2
                        #     board[row][col-i+1] = 0
                        #     g.display_board()
    
        
def move_right():
    
    global board
    global right_start
    for row in range(num_dim1):
        for col in range(num_dim1-1, -1, -1):
            if board[row][col] > 0:
                v2 = board[row][col]
                for i in range(1,4):
                    if col+i < num_dim1:
                        if board[row][col+i] == 0:
                            board[row][col+i-1] = 0
                            board[row][col+i] = v2
                            g.display_board()
                        # elif board[row][col+i] == v2:
                        #     board[row][col+i] = 2*v2
                        #     board[row][col+i-1] = 0
                        #     g.display_board()




def keyPressed():
    
    global done
    if keyCode == DOWN:
        move_down()
        merge_down()
        move_down()
        done = True
    elif keyCode == UP:
        move_up()
        merge_up()
        move_up()
        done = True
    elif keyCode == RIGHT:
        move_right()
        merge_right()
        move_right()
        done = True
    elif keyCode == LEFT:
        move_left()
        merge_left()
        move_left()      
        done = True

    
