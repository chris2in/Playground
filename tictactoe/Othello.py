from msilib.schema import Billboard
from tkinter import *
import numpy as np

size_of_board= 800
numPerRowCol = 8
symbolBlack = '000000'
symbolWhite = 'FFFFFF'


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

        print(self.board)
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
        return (x // (size_of_board//numPerRowCol)+1, y // (size_of_board//numPerRowCol)+1)

    def GridToCord(self,grid):
        Cord = np.array(grid,dtype=int)
        return(size_of_board/numPerRowCol) * Cord+size_of_board/16

    def place(self,Grid):
        for i in range(len(self.board)):
            for o in range(len(self.board[i])):
                print(self.board[i][o],end='    ')
            print()
        if(self.board[Grid[0]][Grid[1]] != 0):
            print("cant do so, it s already ",self.board[Grid[0]][Grid[1]])
        else:    
            if(self.Black_turns):
                #place a black piece
                #which will be mark as 2
                self.board[Grid[0]][Grid[1]] = 2
            else:
                self.board[Grid[0]][Grid[1]]=1
       

        return 0 

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