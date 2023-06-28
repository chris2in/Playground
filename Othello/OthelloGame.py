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

    def ChangeIndicator(self,OthelloObject,newIndi):
        print("changing color to {}".format(newIndi))
        if(int(newIndi) in [1,2,3,4,5]):
            print("changing starts ")
            self.indicator=newIndi

            if(newIndi==1):
                OthelloObject.canvas.itemconfig(self.Rectangle,fill = 'black')
            elif(newIndi ==2):
                OthelloObject.canvas.itemconfig(self.Rectangle,fill = 'white')
            elif(newIndi ==3):
                OthelloObject.canvas.itemconfig(self.Rectangle,fill = 'red')
            elif(newIndi ==4):
                OthelloObject.canvas.itemconfig(self.Rectangle,fill = 'blue')
            elif(newIndi ==5):
                OthelloObject.canvas.itemconfig(self.Rectangle,fill = 'light green')
            


                




    
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
                self.Squares[i].append(Square(self,i,o))
        
        self.Squares[4][3].ChangeIndicator(self,1)
        self.Squares[3][4].ChangeIndicator(self,1)
        self.Squares[3][3].ChangeIndicator(self,2)
        self.Squares[4][4].ChangeIndicator(self,2)


        self.updateBoard()
        print("result is {}".format(self.updateDirection(2,3,[3,4])))

    def convertGridToBoard(self,cor):
        return [int(cor[0]//(size_of_board/numPerRowCol)),int(cor[1]//(size_of_board/numPerRowCol))]

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
                            
                        
                    elif(col >= numPerRowCol-1):
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


        #         self.Squares[row][col].ChangeIndicator(self,self.updateDirection(row,col,directionToCheck))
        # print("herrrrrrrrrrrre")
        # self.Squares[4][6].ChangeIndicator(self,4)

                # self.Squares[5][5].ChangeIndicator(self,5)

            # print()
                
    def updateDirection(self,x,y,direction):
        # direction:
        # up - 1
        # down - 2
        # left - 3
        # right -4
        # results:
        # can be black:3
        # can be white:4
        # can be white or black: 5
        
        available3=False
        available4=False

        result = 0 
        
        for i in direction:
            print("going throught {} now".format(i))
            if(i == 1):
                # newRow = x-1
                # base = self.Squares[x][newRow].indicator
                # if(base == 1 or base ==2 ):
                #     while newRow> 0 and self.Squares[x][newRow]==base:
                #         newRow = newRow -1
                    
                #     if(self.Squares[x][newRow]==1 or self.Squares[x][newRow] ==2 ) and self.Squares
                # for i in range(newBase+1, len(self.Squares[0])):
                #         if(self.Squares[i][y] !=base):
                #             if(self.Squares[i][y]!= 1 and self.Squares[i][y] !=2):
                #                 break 
                #             elif(self.Squares[i][y] ==2):
                #                 return 2
                #             elif(self.Squares[i][y] ==1):
                #                 return 1
                print('place holder for check up')

                # return
            elif(i == 2):
                print('place holder for check down')

                # return

            elif(i==3):
                print("check left")
                newBase = x-1
                
                base = self.Squares[newBase][y].indicator
                for i in range(newBase-1, -1,-1):
                        if(self.Squares[i][y].indicator !=base):
                            if(self.Squares[i][y].indicator!= 1 and self.Squares[i][y].indicator !=2):
                                print('break from check left')
                                break 
                            elif(not available4 and self.Squares[i][y].indicator ==2):
                                available4 = True
                            elif(not available3 and self.Squares[i][y].indicator ==1):
                                available3 =True
                print("exit check left")
            elif(i==4):
                print('checking right')
                newBase = x+1
                # print("x is {} and y is {}, new base is {},{} and the indicator is {}".format(x,y,newBase,y,self.Squares[newBase][y].indicator))
                print("x is {} and y is {}".format(newBase,y))
                base = self.Squares[newBase][y].indicator

                print("base is {}".format(base))
                if(base ==1 or base ==2):
                    print('base is 1 or 2')
                    for i in range(newBase+1, len(self.Squares[0])):
                        print('traversing ')
                        if(self.Squares[i][y].indicator !=base):
                            print('the  value is {}'.format(self.Squares[i][y].indicator))

                            if(self.Squares[i][y].indicator!= 1 and self.Squares[i][y].indicator !=2):
                                print('break')
                                break 
                            elif(not available4 and self.Squares[i][y].indicator ==2):
                                available4 = True
                            elif(not available3 and self.Squares[i][y].indicator ==1):
                                available3 =True

                

        if(available3):
            if(available4):
                return 5
            else:
                return 3
        elif(available4):
            return 4
        else:
            return 0 
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