from tkinter import *


size_of_board = 800
numPerRowCol = 8 
class Square():
    def __init__(self,OthelloObject, x,y,outline = 'dark gray',indicator = 0):  
        global testCounter
        self.x= x
        self.y = y
        self.outline =outline
        self.indicator = indicator
        SquareNum =y*numPerRowCol + x
        length = size_of_board/numPerRowCol
        if(self.indicator == 1):
            self.color = 'black'
        elif(self.indicator == 2):
            self.color = 'white'
        else:
            self.color = 'gray'
        
        self.Rectangle = OthelloObject.canvas.create_rectangle(SquareNum%numPerRowCol*length,
                                                               SquareNum//numPerRowCol*length,
                                                               SquareNum%numPerRowCol*length+length,
                                                               SquareNum//numPerRowCol*length+length, 
                                                               outline='dark gray')
    def changeColor(self,OthelloObject,newColor):
        if(newColor == 'black'):
            self.indicator= 1
        elif(newColor== 'white'):
            self.indicator=2
        elif(newColor == 'red'):
            self.indicator = 3
        elif(newColor == 'blue'):
            self.indicator =4
        elif(newColor == 'light green'):
            self.indicator = 5
        else:
            return 
        
        OthelloObject.canvas.itemconfig(self.Rectangle,fill=newColor)
        # print('called')
        return 
    
    def getX(self):
        return self.x
    def getY(self):
        return self.y

class Othello():

    def __init__(self):

        # true for black and false for white
        self.turn = True
        
        self.window= Tk()

        self.window.title("Othello")

        self.canvas = Canvas(self.window, width = size_of_board, height= size_of_board, bg = 'lightgray')
        self.canvas.pack()

        self.window.bind('<Button-1>',self.click)

        self.Squares= []

        length = size_of_board/numPerRowCol
        for i in range(numPerRowCol):
            self.Squares.append([])
            for o in range(numPerRowCol):
                self.Squares[i].append(Square(self,o,i))
        
        self.Squares[4][3].changeColor(self,'black')
        self.Squares[3][4].changeColor(self,'black')
        self.Squares[3][3].changeColor(self,'white')
        self.Squares[4][4].changeColor(self,'white')


        self.updateBoard()

    def convertGridToBoard(self,cor):
        return [int(cor[1]//(size_of_board/numPerRowCol)),int(cor[0]//(size_of_board/numPerRowCol))]

    def updateBoard(self):
        # for row in range(len(self.Squares)):
        #     for col in range(len(self.Squares[row])):
        #         print(self.Squares[col][row].indicator,end='\t')
        #     print()

        for row in range(len(self.Squares)):
            for col in range(len(self.Squares[row])):
                # print("{},{}".format(row,col),end = '\t')
                # if(self.Squares[row][col].getX() == row and self.Squares[row][col].getY()== col):
                #     continue
                # else:
                #     break
                if(not (self.Squares[row][col]==1 or self.Squares[row][col] == 2)):
                    directionToCheck = []
                    # up - 1
                    # down - 2
                    # left - 3
                    # right -4

                    if(col == 0 ):
                        directionToCheck.append(4)
                        if(row == 0):
                            directionToCheck.append(2)
                        elif(row == numPerRowCol):
                            directionToCheck.append(1)
                        else:
                            directionToCheck.append(2)
                            directionToCheck.append(1)
                            
                        
                    elif(col == numPerRowCol-1):
                        directionToCheck.append(3)
                        if(row == 0):
                            directionToCheck.append(2)
                        
                        elif(row == numPerRowCol):
                            directionToCheck.append(1)
                        
                        else:
                            directionToCheck.append(2)
                            directionToCheck.append(1) 
                        
                    else:
                        directionToCheck.append(1)
                        directionToCheck.append(2)
                        directionToCheck.append(3)
                        directionToCheck.append(4)
                self.updateDirection(row,col,directionToCheck)
            # print()
                
    def updateDirection(self,x,y,direction):
        # direction:
        # up - 1
        # down - 2
        # left - 3
        # right -4
        # results:
        # can be black:3
        result = 0 
        
        for i in direction:
            if(i == 1):
                # newRow = x-1
                # base = self.Squares[x][newRow].indicator
                # if(base == 1 or base ==2 ):
                #     while newRow> 0 and self.Squares[x][newRow]==base:
                #         newRow = newRow -1
                    
                #     if(self.Squares[x][newRow]==1 or self.Squares[x][newRow] ==2 ) and self.Squares
                    
                return
            elif(i == 2):
                return

            elif(i==3):
                return
            
            elif(i==4):
                return
# work point
    def click(self,event):

        boardPosition = self.convertGridToBoard([event.x,event.y])
        print(boardPosition)


        # if(not validMove())
        if(self.turn):
            self.Squares[boardPosition[0]][boardPosition[1]].changeColor(self,'black')
            self.turn = not self.turn
        else:
            self.Squares[boardPosition[0]][boardPosition[1]].changeColor(self,'white')
            self.turn = not self.turn

        self.updateBoard()

    def mainloop(self):
        self.window.mainloop()
game_instance = Othello()
game_instance.mainloop()