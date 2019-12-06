import os
import random
path = os.getcwd()



size_game = 1000
n1 = 0
down_start = False
up_start = False
right_start = False
left_start = False

col_list = []
row_list = []
info_loc = {}
info_value = {}

num_dim1 = 4
size_tile1 = 100
bold_edge1 = 6

size_edge1 = size_tile1/bold_edge1
board=[]

class Tile:
    def __init__(self, r, c, value, index):
        self.r = r
        self.c = c
        self.y = 100+size_edge1+(size_edge1+size_tile1)*self.r
        self.x = 100+size_edge1+(size_edge1+size_tile1)*self.c
        self.value = value
        self.index= index
        
    def display(self):

        if self.value == 2:
            fill(238,228,219)
            rect(self.x,self.y,size_tile1,size_tile1)
        elif self.value == 4:
            fill(237,224,203)
            rect(self.x,self.y,size_tile1,size_tile1)
        elif self.value == 8:
            fill(242,176,129)
            rect(self.x,self.y,size_tile1,size_tile1)
        elif self.value == 16:
            fill(245,148,107)
            rect(self.x,self.y,size_tile1,size_tile1)
        elif self.value == 32:
            fill(247,124,101)
            rect(self.x,self.y,size_tile1,size_tile1)
        elif self.value == 64:
            fill(247,93,69)
            rect(self.x,self.y,size_tile1,size_tile1)
        elif self.value == 128:
            fill(237,207,128)
            rect(self.x,self.y,size_tile1,size_tile1)
        elif self.value == 256:
            fill(237,204,110)
            rect(self.x,self.y,size_tile1,size_tile1)
        elif self.value == 512:
            fill(237,200,97)
            rect(self.x,self.y,size_tile1,size_tile1)
        elif self.value == 1024:
            fill(238,190,75)
            rect(self.x,self.y,size_tile1,size_tile1)
        elif self.value == 2048:
            fill(195,139,71)
            rect(self.x,self.y,size_tile1,size_tile1)
            
        if self.value <= 4:
            textSize(50)
            fill(119,110,102)
            text(str(self.value), self.x+35, self.y+65)
        else:
            textSize(50)
            fill(249,246,242)
            text(str(self.value), self.x+35, self.y+65)

class Game:
    
    def __init__(self, num_dim, size_tile, bold_edge):
        self.num_dim = num_dim
        self.size_tile = size_tile
        self.bold_edge = bold_edge
        self.size_edge = 100/self.bold_edge
        self.size_board = self.size_edge+(self.size_edge+self.size_tile)*self.num_dim
        
    def display_board(self):
        noStroke()
        fill(187,173,161)
        rect(100, 100, self.size_board, self.size_board, 10)
        for i in range(self.num_dim):
            for j in range(self.num_dim):
                noStroke()
                fill(205,193,181)
                rect(100+self.size_edge+(self.size_edge+self.size_tile)*j, 100+self.size_edge+(self.size_edge+self.size_tile)*i, self.size_tile, self.size_tile, 5)
    
    def generate_tile(self):
        
        global n1
        if len(col_list) == 0:
            r1 = random.randint(0, num_dim1-1)
            c1 = random.randint(0, num_dim1-1)
            col_list.append(c1)
            row_list.append(r1)
            r1 = random.randint(0, num_dim1-1)
            c1 = random.randint(0, num_dim1-1)
            while True:
                cnt = 0
                for i in range(len(col_list)):
                    if (row_list[i] == r1) and (col_list[i] == c1) :
                        r1 = random.randint(0, num_dim1-1)
                        c1 = random.randint(0, num_dim1-1)
                        break
                    else:
                        cnt += 1
                        continue
                if cnt == len(col_list):
                    break
                else:
                    continue
            col_list.append(c1)
            row_list.append(r1)
            for k in range(len(col_list)):
                v1 = random.choice([2,4])
                n1 += 1
                info_loc[n1] = (row_list[k],col_list[k])
                info_value[n1] = v1
            
        else:
            r1 = random.randint(0, num_dim1-1)
            c1 = random.randint(0, num_dim1-1)
            while True:
                cnt = 0
                for i in range(len(col_list)):
                    if (row_list[i] == r1) and (col_list[i] == c1) :
                        r1 = random.randint(0, num_dim1-1)
                        c1 = random.randint(0, num_dim1-1)
                        break
                    else:
                        cnt += 1
                        continue
                if cnt == len(col_list):
                    break
                else:
                    continue
            col_list.append(c1)
            row_list.append(r1)  
            v1 = random.choice([2,4])
            n1 += 1
            info_loc[n1] = (r1,c1)
            info_value[n1] = v1
    
    
    def display_tiles(self):
        for key1 in info_loc:
            loc = info_loc[key1]
            r2 = loc[0]
            c2 = loc[1]
            v2 = info_value[key1]
            Tile(r2,c2,v2,key1).display()
            

g = Game(num_dim1, size_tile1, bold_edge1)                            
                                                                                                
def move_down():
    
    global down_start
    if down_start == True:
        for i1 in range(num_dim1-1, -1, -1):
            for j1 in range(num_dim1):
                if (i1,j1) not in info_loc.values():
                    continue
                else:
                    n2 = list(info_loc.keys())[list(info_loc.values()).index((i1,j1))]
                    v2 = info_value[n2]
                    while i1+1 < num_dim1 and (i1+1,j1) not in info_loc.values():
                        i1 = i1+1
                        info_loc.pop(n2)
                        info_loc[n2] = (i1,j1)
                        g.display_board()
                        g.display_tiles()
                                    
                        
def move_up():
    
    global up_start
    if up_start == True:
        for i2 in range(num_dim1):
            for j2 in range(num_dim1):
                if (i2,j2) not in info_loc.values():
                    continue
                else:
                    n2 = list(info_loc.keys())[list(info_loc.values()).index((i2,j2))]
                    v2 = info_value[n2]
                    while i2-1 > -1 and (i2-1,j2) not in info_loc.values():
                        i2 = i2-1
                        info_loc.pop(n2)
                        info_loc[n2] = (i2,j2)
                        g.display_board()
                        g.display_tiles() 
                        
                                 
def move_left():
        
    global left_start
    if left_start == True:
        for j3 in range(num_dim1):
            for i3 in range(num_dim1):
                if (i3,j3) not in info_loc.values():
                    continue
                else:
                    n2 = list(info_loc.keys())[list(info_loc.values()).index((i3,j3))]
                    v2 = info_value[n2]
                    while j3-1 > -1 and (i3,j3-1) not in info_loc.values():
                        j3 = j3-1
                        info_loc.pop(n2)
                        info_loc[n2] = (i3,j3)
                        g.display_board()
                        g.display_tiles()      
                        
                        
def move_right():
    
    global right_start
    if right_start == True:
        for j4 in range(num_dim1-1, -1, -1):
            for i4 in range(num_dim1):
                if (i4,j4) not in info_loc.values():
                    continue
                else:
                    n2 = list(info_loc.keys())[list(info_loc.values()).index((i4,j4))]
                    v2 = info_value[n2]
                    while j4+1 < num_dim1 and (i4,j4+1) not in info_loc.values():
                        j4 = j4+1
                        info_loc.pop(n2)
                        info_loc[n2] = (i4,j4)
                        g.display_board()
                        g.display_tiles()
              
                
def keyPressed():
    global down_start
    global up_start
    global right_start
    global left_start
    if keyCode == DOWN:
        down_start = True
    elif keyCode == UP:
        up_start = True
    elif keyCode == RIGHT:
        right_start = True
    elif keyCode == LEFT:
        left_start = True

def keyReleased():
    global down_start
    global up_start
    global right_start
    global left_start
    if keyCode == DOWN:
        down_start = False
    elif keyCode == UP:
        up_start = False
    elif keyCode == RIGHT:
        right_start = False
    elif keyCode == LEFT:
        left_start = False         
       

g = Game(num_dim1, size_tile1, bold_edge1)

def settings():
    size(size_game, size_game)
    
def setup():
    background(250,248,240)
    g.display_board()
    g.generate_tile()
    g.display_tiles()
    print(info_loc)
    print(info_value)

def draw():
    global up_start
    global down_start
    global right_start
    global left_start
    move_down()
    move_up()
    move_right()
    move_left()
