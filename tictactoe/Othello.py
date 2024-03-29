
from msilib.schema import Billboard
from tkinter import *
import numpy as np

import checkAviTest


size_of_board= 800
numPerRowCol = 8
symbol_size= (size_of_board/numPerRowCol - size_of_board/numPerRowCol)/2

#   1 for white
#   2 for black
#   3 for available for white
#   4 for available for black 
#   5 for available for both 

symbolBlack = '#000000'
symbolWhite = '#FFFFFF'
symbolAVIWhite= '#CCFFFF'
symbolAVIBlack = '#FFCCCC'
symbolAVIBoth = '#FFFFCC'
symbol_thickness= 2
DEBUGTEST = True

class Othello():
    
    def __init__(self):
        self.window = Tk()
        # self.window.attributes('-fullscreen',True)
        self.window.title("Try Othelowsomehting")

        self.canvas = Canvas(self.window, width= size_of_board,height=size_of_board,bg = 'lightgray')
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
        self.generateAviSpot()
        
        self.render()
        # print(self.board)
        # for i in range(len(self.board)):
        #     for o in range(len(self.board[i])):
        #         print(self.board[i][o],end='    ')
        #     print()
        self.window.bind('<Key>',self.key_input)

        self.availableForWhite = True
        self.availableForBlack = True
        
    def flip(self,board,row,col,piece):
        #takes in the 2d array board, x, and y
        #   returns the udpated board 

        score = 0
        # board [0][0] = 20
        widthMAX  = len(board[0])
        heightMAX = len(board)-1

        # anchor = piece
        board[row][col]= piece
        
        # endWell =False
        if( col < widthMAX -1 ) :
            #   list to traverse
            traverseList = board[row][col+1:]
            directionFlip = 0 
            # print("start checkign right ")
            for i in traverseList:
                if( i> 0 and i < 3 and i != piece):
                    # print("one pass, next one")
                    directionFlip +=1
                    
                else:
                    # print("stopped")
                    if(i == piece):
                        # print("we get to flip some")
                        for index in range(directionFlip):
                            board[row][col+index+1] = piece
                        score += directionFlip
        
        if( col > 1):
            traverseList = board[row][0:col]
            traverseList.reverse()
            directionFlip = 0
            # print("reverse list is {}".format(traverseList))
            for i in traverseList:
                if( i > 0 and i < 3 and i != piece):
                    directionFlip +=1
                else:
                    if( i == piece):
                        for index in range(directionFlip):
                            board[row][col-index-1] = piece
                        score  += directionFlip
        

        if(row > 1 ):
            directionFlip = 0

            traverseList = []
            for i in range(row-1,-1,-1):
                traverseList.append(board[i][col])
            for i in traverseList:
                if( i > 0 and i < 3 and i != piece):
                    directionFlip +=1
                else:

                    if( i == piece):
                        for index in range(directionFlip):
                            board[row-index-1][col] = piece
                        print("fliping {},{} to {}".format(row+index+1,col,piece))
                        score  += directionFlip
        
        if( row < heightMAX -1):
            directionFlip = 0

            traverseList = []
            for i in range(0,row+1):
                traverseList.append(board[row+i+1][col])
            print(traverseList)

            for i in traverseList:
                if( i > 0 and i < 3 and i != piece):
                    directionFlip +=1
                else:
                    if( i == piece):
                        for index in range(directionFlip):
                            board[row+index+1][col] = piece
                        score  += directionFlip
        return score 


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
        
        if(self.board[x][y] > 0 and self.board[x][y]<3):
            print("cant do so, it s already ",self.board[x][y])
        elif(self.board[x][y]==0):
            print("not available")
        elif((self.board[x][y] == 5 or self.board[x][y] == 3) and not self.Black_turns):
            # self.board[x][y] = 1
            self.flip(self.board,x,y,1)

            self.Black_turns = not self.Black_turns

        elif((self.board[x][y] == 5 or self.board[x][y] == 4) and self.Black_turns):
            # self.board[x][y] = 2
            self.flip(self.board,x,y,2)
            self.Black_turns = not self.Black_turns

        else:    
            print("?")
        
            
        if(DEBUGTEST):
            print('beginning of this turn')
            for i in range(len(self.board)):
                    for o in range(len(self.board[i])):
                        print(self.board[i][o],end='    ')
                    print()
            print('end of this turn')
        self.generateAviSpot()
        self.render()
        # self.checkAvi(0,0)
        return 0 

    def refreshBoard(self,x,y,piece):
        # when a piece(color) is place at current location (x,y)
        # it must be available spot for to be place 
        # first check left
        return 0
    
    def generateAviSpot(self):
        for i in range(len(self.board)):
            for o in range(len(self.board[i])):
                if(self.board[i][o] != 1 and self.board[i][o] != 2):
                    self.board[i][o] = checkAviTest.checkavi(self.board,i,o)  

        return 0

    '''# def checkAvi(self,i,o):
    #     blackAvi = False
    #     whiteAvi = False

        

    #     if (i == 0 ):

    #         #   when checking the top left corner 
    #         if(o == 0):

    #             if(self.board[0][1]>0 and self.board[0][1]< 3):
    #                 nextSpot = self.board[0][1]
    #             #   checking right-direction 

    #                 # there are six more spot to check 
    #                 for col in range(6):

    #                     #   need fix here
    #                     #   no point always getting first 6
    #                     #   need to make it dynamic 
    #                     #   let s start working on different cases and automatic tests
    #                     #   in python where reads array for test



    #                     #   if next one to [0][1] is same, continue until finding the different color one, then set Avi
    #                     #       otherwise, nothing happens 
    #                     # print (type(self.board[0][col]))
    #                     # print("TTT", col)
    #                     # print(self.board[0][col])
    #                     if int(self.board[0][col]) > 0 and int(self.board[0][col])<3 and nextSpot != self.board[0][col]:
    #                         if(nextSpot==1):
    #                             if (DEBUGTEST):
    #                                 print("black avi")
    #                             blackAvi=True
    #                             break
    #                         else:
    #                             if (DEBUGTEST):
    #                                 print("white avi 1")
    #                             whiteAvi=True
    #                             break
    #                         if(blackAvi and whiteAvi):
    #                             break
                    
    #                 if(not ( blackAvi and whiteAvi)):
    #                     downSpot = self.board[1][0]
    #                     for row in range(6):
    #                         if self.board[row][0] >0 and self.board[row][0]<3 and  downSpot !=self.board[row][0]:
                            
    #                             if(not blackAvi and downSpot==1):
    #                                 if (DEBUGTEST):
    #                                     print("black avi")
    #                                 blackAvi =True
    #                                 break
    #                             elif(not whiteAvi and downSpot==2):
    #                                 if (DEBUGTEST):
    #                                     print("white avi 2")
    #                                 whiteAvi = True
    #                                 break
                                

                
                                    
    #         elif(o==7):
    #             return 0
    #         else:
    #             return 0

    #     elif(i == 7):
    #         return 0
    #     else:
    #         return 0 
    #     if(blackAvi):
    #         if(whiteAvi):
    #             self.board[i][o]= 5
    #         else:
    #             self.board[i][o]= 3
    #     elif(whiteAvi):
    #         self.board[i][o]=4


        #   run test here, to see if 0,0 will update according to pieces on the right and below,
        #   case one: 1,2,2,2,1
        #   case two: 1,2,1
        #   case three: 1,0,0,0
        #   case four: 2,1,1,2
        #   case five: 2,1,1,1,1
        #   case six: 0,0,0,0
        #   case seven: 1,1
        #   pass the case with 5
        
        '''

        

         




    def render(self):
        
        for i in range(len(self.board)):
            for o in range(len(self.board[i])):
                Cord=self.GridToCord((o,i))

                x=Cord[0]
                y=Cord[1]
                x1 = x+size_of_board/numPerRowCol -5
                y1 =y+size_of_board/numPerRowCol -5
                valueOfGrid = self.board[i][o]
                if(valueOfGrid!=0):
                    
                    if(valueOfGrid==1):
                        self.canvas.create_oval(x+5,y+5,x1,y1,width=symbol_thickness,outline=symbolBlack,fill=symbolWhite)
                    elif(valueOfGrid ==2):
                        self.canvas.create_oval(x+3,y+3,x1,y1,width=symbol_thickness,outline=symbolBlack,fill=symbolBlack)
                    elif((valueOfGrid == 3  and not self.Black_turns) or valueOfGrid ==5):
                        self.canvas.create_oval(x+3,y+3,x1,y1,width=symbol_thickness,outline=symbolBlack,fill=symbolAVIWhite)
                    elif((valueOfGrid == 4  and self.Black_turns)or valueOfGrid ==5):
                        self.canvas.create_oval(x+3,y+3,x1,y1,width=symbol_thickness,outline=symbolBlack,fill=symbolAVIBlack)
                    else:
                        self.canvas.create_oval(x+3,y+3,x1+2,y1+2,width=symbol_thickness,outline="#d3d3d3",fill="#d3d3d3")




                


    def click(self,event):
        self.place(self.CordToGrid(event.x,event.y))
        self.isGameOver()

    def key_input(self,event):
        print(event.keysym)

       



        userInput = event.keysym
        if(userInput in ['1','2','3','4','5','6','7','8']):
            # print('i got ',userInput)
            # print('going to pring ',userInput, 'row', self.board[int(userInput)-1])
            queryList = self.board[int(userInput)-1]
            # print('query over')
            # print(queryList)
            for i in range(len(queryList)):
                print(queryList[i], end='\t')
            print("")
        elif(userInput in ['q','w','e','r','t','y','u','i']):
            
            
            offset = ['q','w','e','r','t','y','u','i'].index(userInput)
            for i in range(len(self.board)):
                print(self.board[i][offset],end='\t')
            print("")
            
        elif(userInput == "p"):
            for i in range(len(self.board)):
                for o in range(len(self.board[i])):
                    print(self.board[i][o],end='\t')
                print()


    def initialize_board(self):
        for i in range(numPerRowCol-1):
            self.canvas.create_line((i + 1) * size_of_board / numPerRowCol-1, 0, (i + 1) * size_of_board / numPerRowCol-1, size_of_board)

        for i in range(numPerRowCol-1):
            self.canvas.create_line(0, (i + 1) * size_of_board / numPerRowCol-1, size_of_board, (i + 1) * size_of_board / numPerRowCol-1)

    def mainloop(self):
        self.window.mainloop()

# print("S")
# checkAviTest.checkavi()

game = Othello()
game.mainloop()