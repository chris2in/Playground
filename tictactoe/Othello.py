from distutils.DEBUGTEST import DEBUGTEST
from msilib.schema import Billboard
from tkinter import *
import numpy as np

size_of_board= 800
symbol_size= (size_of_board/8 - size_of_board/8)/2
numPerRowCol = 8
symbolBlack = '#000000'
symbolWhite = '#FFFFFF'
symbolAVIWhite= '#0ABAB5'
symbolAVIBlack = '#ff0000'
symbol_thickness= 5
DEBUGTEST = False

class Othello():
    
    def __init__(self):
        self.window = Tk()
        # self.window.attributes('-fullscreen',True)
        self.window.title("Try Othelowsomehting")

        self.canvas = Canvas(self.window, width= size_of_board,height=size_of_board)
        self.canvas.pack()

        self.window.bind('<Button-1>',self.click)

        self.initialize_board()
        self.Black_turns = True

        self.board = [[0]*numPerRowCol for i in range(numPerRowCol)]
        # print(self.board[3][3])
        self.board[3][3] =1
        self.board[4][4] =1
        self.board[3][4] =2
        self.board[4][3] =2

        # print(self.board)
        # for i in range(len(self.board)):
        #     for o in range(len(self.board[i])):
        #         print(self.board[i][o],end='    ')
        #     print()

        self.availableForWhite = True
        self.availableForBlack = True
        


    def isGameOver(self):
        gameOver =False
        noSpace = False
        availableGrid = []
        for i in range(len(self.board)):
            for o in range(len(self.board[i])):
                if self.board[i][o] == 0:
                    availableGrid.append((i,o))
                    #instead of this, do verification whether or not it s valid for move
        
        # print(availableGrid)
             
            
                
    def isWinner(self,player):
        return 0

    # # change  s
    # def click(self, event):
    #     grid_position = [event.x,event.y]
    #     position = self.covertToPosition(grid_position)

    # def convertToposition(self, grid_position):
    #     grid_position = np.array(grid_position)
    #     return np.array(grid_position // (size_of_board/3),dtype = int)
    def CordToGrid(self,x,y):
        return (y // (size_of_board//numPerRowCol)+1, x // (size_of_board//numPerRowCol)+1)

    def GridToCord(self,grid):
        x=grid[0]
        y=grid[1]
        # print('inGridTOCordFuntion,',x,' and ',y)
        return (x*(size_of_board/numPerRowCol),y*(size_of_board/numPerRowCol))
        # return (x*(size_of_board/numPerRowCol)+size_of_board/numPerRowCol/2,y*(size_of_board/numPerRowCol)+size_of_board/numPerRowCol/2) 
        # Cord = np.array(grid,dtype=int)
        # return(size_of_board/numPerRowCol) * Cord+size_of_board/16

    def place(self,Grid):
        x=Grid[0]-1
        y=Grid[1]-1
        
        if(self.board[x][y] != 0 and self.board[x][y] != 3 and self.board[x][y] !=4):
            print("cant do so, it s already ",self.board[x][y])
        else:    
            if(self.Black_turns):
                #place a black piece
                #which will be mark as 2
                self.refreshBoard(x,y,2)
                # self.board[x][y] = 2
            else:
                # self.board[x][y]=1
                self.refreshBoard(x,y,1)
            self.Black_turns = not self.Black_turns
            
        if(DEBUGTEST):
            print('beginning of this turn')
            for i in range(len(self.board)):
                    for o in range(len(self.board[i])):
                        print(self.board[i][o],end='    ')
                    print()
            print('end of this turn')
        self.render()
        return 0 

    def refreshBoard(self,x,y,piece):
        return 0

    def render(self):
        
        for i in range(len(self.board)):
            for o in range(len(self.board[i])):
                Cord=self.GridToCord((o,i))

                x=Cord[0]
                y=Cord[1]
                valueOfGrid = self.board[i][o]
                if(valueOfGrid!=0):
                    # print('x',x)
                    # print('y',y)
                    if(valueOfGrid==1):

                        
                        self.canvas.create_oval(x,y,x+size_of_board/numPerRowCol,y+size_of_board/numPerRowCol,width=symbol_thickness,outline=symbolBlack,fill=symbolWhite)
                    elif(valueOfGrid ==2):
                        self.canvas.create_oval(x,y,x+size_of_board/numPerRowCol,y+size_of_board/numPerRowCol,width=symbol_thickness,outline=symbolBlack,fill=symbolBlack)
                    elif(valueOfGrid == 3 and not self.Black_turns):
                        self.canvas.create_oval(x,y,x+size_of_board/numPerRowCol,y+size_of_board/numPerRowCol,width=symbol_thickness,outline=symbolBlack,fill=symbolAVIWhite)
                    elif(valueOfGrid == 4 and self.Black_turns):
                        self.canvas.create_oval(x,y,x+size_of_board/numPerRowCol,y+size_of_board/numPerRowCol,width=symbol_thickness,outline=symbolBlack,fill=symbolAVIBlack)



                


    def click(self,event):
        self.place(self.CordToGrid(event.x,event.y))
        self.isGameOver()

        


    def initialize_board(self):
        for i in range(numPerRowCol-1):
            self.canvas.create_line((i + 1) * size_of_board / numPerRowCol-1, 0, (i + 1) * size_of_board / numPerRowCol-1, size_of_board)

        for i in range(numPerRowCol-1):
            self.canvas.create_line(0, (i + 1) * size_of_board / numPerRowCol-1, size_of_board, (i + 1) * size_of_board / numPerRowCol-1)

    def mainloop(self):
        self.window.mainloop()


game = Othello()
game.mainloop()