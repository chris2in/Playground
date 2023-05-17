from tkinter import *


size_of_board = 800
numPerRowCol = 8 
class Square():
    def __init__(self,OthelloObject, x,y,outline = 'dark gray',indicator = 0):  
        self.x= x
        self.y = y
        self.outline =outline
        self.indicator = 1
        SquareNum =y*numPerRowCol + x
        length = size_of_board/numPerRowCol
        
        if(self.indicator == 1):
            self.color = 'black'
        elif(self.indicator == 2):
            self.color = 'white'
        else:
            self.color = 'gray'
        OthelloObject.canvas.create_rectangle(SquareNum%numPerRowCol*length,SquareNum//numPerRowCol*length,SquareNum%numPerRowCol*length+length,SquareNum//numPerRowCol*length+length, outline='dark gray')
    def changeColor(self,newColor):
        
        return 
    
    def getX(self):
        return self.x
    def getY(self):
        return self.y

class Othello():

    def __init__(self):
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
                




    def convertGridToBoard(self):
        return 

    def click(self,event):

        boardPosition = self.convertGridToBoard()
        print("//")
        print(self.Squares[2][3].getX())


    def mainloop(self):
        self.window.mainloop()
game_instance = Othello()
game_instance.mainloop()