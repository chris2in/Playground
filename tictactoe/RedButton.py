from tkinter import *
from threading import Timer 

size_of_board = 800
numPerRowCol = 8
symbol_size= (size_of_board/numPerRowCol - size_of_board/numPerRowCol)/2





class Othello():

    def __init__(self):
        self.window = Tk()
        
        self.window.title("second attemp")

        self.canvas = Canvas(self.window, width = size_of_board, height = size_of_board, bg = 'lightgray'   )
        self.canvas.pack()

        self.window.bind('<Button-1>', self.click)

        # self.firstSquare = self.canvas.create_rectangle(0,0,300,300)
        self.Square = []
        self.Board = []
        #   in board, black is 1, available for black is 3
        #             white is 2, available for white is 4
        #             available for both is 5 


        self.initialize_board()

        self.currentColor = True

        # self.initialize_board()

    
    def initialize_board(self):
        length = size_of_board/numPerRowCol
        for i in range(numPerRowCol*numPerRowCol):
            print("x goes from {} to {}, y goes from  {} to {}".format(i//numPerRowCol*length,i//numPerRowCol*length+length,i%numPerRowCol*length,i%numPerRowCol*length+length))

            # self.Square.append(self.canvas.create_rectangle(i%numPerRowCol*length,i//numPerRowCol*length,i%numPerRowCol*length+length,i//numPerRowCol*length+length))


            # if(i%3==0):
            #     self.Square.append(self.canvas.create_rectangle(i%numPerRowCol*length,i//numPerRowCol*length,i%numPerRowCol*length+length,i//numPerRowCol*length+length,fill='green'))
            # elif(i%3==1):
            #     self.Square.append(self.canvas.create_rectangle(i%numPerRowCol*length,i//numPerRowCol*length,i%numPerRowCol*length+length,i//numPerRowCol*length+length,fill='blue'))

            # else:
            #     self.Square.append(self.canvas.create_rectangle(i%numPerRowCol*length,i//numPerRowCol*length,i%numPerRowCol*length+length,i//numPerRowCol*length+length,fill='yellow'))

        for i in range(numPerRowCol):
            self.Square.append([])
            # print(self.Square)
            self.Board.append([])

            for o in range(numPerRowCol):
                indicator = i*8+o
                self.Square[i].append(self.canvas.create_rectangle(indicator%numPerRowCol*length,indicator//numPerRowCol*length,indicator%numPerRowCol*length+length,indicator//numPerRowCol*length+length, outline='dark gray'))
                self.Board[i].append(0)
            print(self.Board)


        self.canvas.itemconfig(self.Square[3][3],fill = 'white')
        self.Board[3][3] = 2
        self.canvas.itemconfig(self.Square[4][4],fill = 'white')
        self.Board[4][4] = 2

        self.canvas.itemconfig(self.Square[3][4],fill = 'black')
        self.Board[3][4] = 1
        
        self.canvas.itemconfig(self.Square[4][3],fill = 'black')
        self.Board[4][3] = 1
        # self.placeMove(3,3,"white")

        print("going to start update")
        self.updateAvilableMove()
        print('update finished')
        


        # 27 while

        # 28 black
        # self.canvas.itemconfig(self.Square[1],fill='blue')
        # self.canvas.itemconfig(self.Square[2],fill='green')
        # self.canvas.itemconfig(self.Square[3],fill='yellow')


        # self.canvas.itemconfig(self.Square[27],fill='white')
        # self.canvas.itemconfig(self.Square[36],fill='white')
        # self.canvas.itemconfig(self.Square[28],fill='black')
        # self.canvas.itemconfig(self.Square[35],fill='black')

        print(self.Square)
    
    def placeMove(self,x,y,color):
        # if(self.Board[x][y]==5  or  (self.Board[x][y] == 3 and color =='black') or (self.Board[x][y] ==4 and color == 'white')):
        #     self.flip(x,y,color)
        # else:
        #     return 
        self.canvas.itemconfig( self.Square[x][y],fill=color)
        if(color == 'black'):
            self.Board[x][y] = 1
        else:
            self.Board[x][y] = 2

        
        return 


        # self.Board[x][y] 
    #   work point 3: do we still need this method? 

    def flip(self,x,y,color):
        self.canvas.itemconfig(self.Square[x][y],fill = color)
        if(color == 'white'):
            self.Board[x][y] = 2

        else:
            self.Board[x][y] = 1
        return 

        #update the color in self board 
    #   work point 2: able to flip and change color, updat the self.board


    def updateAvilableMove(self):
        #   this go over all the row number

        for row in len(self.Board):

            #   create temp row holder to save access time 
            tempRow = self.Board[row]
            
            for col in len(tempRow):
                #   this go over all the element in a row
                if (not(self.board[row][col] ==1 or self.Board[row][col]==2)):
                    directions = []

                    if(row == 0):
                        directions.append('right')
                    elif(row == numPerRowCol-1):
                        directions.append('left')
                    else:
                        directions.append('left')
                        directions.append('right')
                    if(col == 0):
                        directions.append('down')
                    elif(col == numPerRowCol-1):
                        directions.append('up')
                    else:
                        directions.append('up')
                        directions.append('down')
                self.checkAvailbity(row,col,directions)


        return 
    



        
    #   work point 1: update 3,4,5 indicated available moves for each part of the board

    def checkAvailbity(self,row,col,directions):
        black = False
        white = False

        
        for i in directions:
            if(i == 'up'):
                back = self.Board[row+1][col]
                if(back ==1 or back ==2):
                    if(self.Board[row-1][col] ==back):
                        return
                    else:
                        if(back == 2):
                            white = True
                        else:
                            black = True


            elif(i == 'down'):
                back = self.Board[row-1][col]
                if(back ==1 or back ==2):
                    if(self.Board[row+1][col] ==back):
                        return
                    else:
                        if(back == 2):
                            white = True
                        else:
                            black = True
                    if(black and white):
                        self.Board[row][col] = 5
                        return 
            elif( i == 'left'):
                back = self.Board[row][col+1]
                if(back ==1 or back ==2):
                    if(self.Board[row-1][col] ==back):
                        return
                    else:
                        if(back == 2):
                            white = True
                        else:
                            black = True
                    if(black and white):
                        self.Board[row][col] = 5
                        return 
                    

            elif(i == 'right '):
                back = self.Board[row][col-1]
                if(back ==1 or back ==2):
                    if(self.Board[row+1][col] ==back):
                        return
                    else:
                        if(back == 2):
                            white = True
                        else:
                            black = True
                    if(black and white):
                        self.Board[row][col] = 5
                        return 
            else:
                if(white):
                    self.Board[row][col] = 4
                elif(black):
                    self.Board[row][col]=3
                else:
                    self.Board[row][col]=0
            
        return 






    def mainloop(self):
        self.window.mainloop()

    # def changeColor(self,shape):
        
    #     self.canvas.itemconfig(shape,fill='green')
    #     # print()

    def click(self, event):
        # self.changeColor(self.firstSquare)
        # print(event.x,"   ",event.y)

        for i in range(len(self.Board)):
            for o in range(len(self.Board[i])):
                print(self.Board[i][o],end='\t')
            print()



        boardPosition = self.convertGridToBoard([event.x,event.y])
        print(boardPosition)
        if(self.validMove(self.convertGridToBoard([event.x,event.y]))):
            if(self.currentColor):
                self.placeMove(boardPosition[0],boardPosition[1],'black')
                # self.canvas.itemconfig( self.Square[boardPosition[0]][boardPosition[1]],fill='black')
            else:
                self.placeMove(boardPosition[0],boardPosition[1],'white')

                # self.canvas.itemconfig( self.Square[boardPosition[0]][boardPosition[1]],fill='white')

            self.currentColor = not self.currentColor
        else:
            print("not valid move")

        for i in range(len(self.Board)):
            for o in range(len(self.Board[i])):
                print(self.Board[i][o],end='\t')
            print()
        return 
    

    def validMove(self,list):
        return True

    def convertGridToBoard(self,cor):
        # print ([int(cor[0]//(size_of_board/numPerRowCol)),int(cor[1]//(size_of_board/numPerRowCol))])
        return [int(cor[1]//(size_of_board/numPerRowCol)),int(cor[0]//(size_of_board/numPerRowCol))]


game_instance = Othello()
game_instance.mainloop()