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
        self.initialize_board()


        # self.initialize_board()

    
    def initialize_board(self):
        length = size_of_board/numPerRowCol
        for i in range(numPerRowCol*numPerRowCol):
            print("x goes from {} to {}, y goes from  {} to {}".format(i//numPerRowCol*length,i//numPerRowCol*length+length,i%numPerRowCol*length,i%numPerRowCol*length+length))
            if(i%3==0):
                self.Square.append(self.canvas.create_rectangle(i//numPerRowCol*length,i%numPerRowCol*length,i//numPerRowCol*length+length,i%numPerRowCol*length+length,fill='green'))
            elif(i%3==1):
                self.Square.append(self.canvas.create_rectangle(i//numPerRowCol*length,i%numPerRowCol*length,i//numPerRowCol*length+length,i%numPerRowCol*length+length,fill='blue'))
            else:
                self.Square.append(self.canvas.create_rectangle(i//numPerRowCol*length,i%numPerRowCol*length,i//numPerRowCol*length+length,i%numPerRowCol*length+length,fill='yellow'))

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
    


    def mainloop(self):
        self.window.mainloop()

    # def changeColor(self,shape):
        
    #     self.canvas.itemconfig(shape,fill='green')
    #     # print()

    def click(self, event):
        # self.changeColor(self.firstSquare)
        # print(event.x,"   ",event.y)
        boardPosition = int(self.convertGridToBoard([event.x,event.y]))
        self.canvas.itemconfig( self.Square[boardPosition],fill='red')
        return 
    
    def convertGridToBoard(self,cor):


        return (cor[0]//(size_of_board/numPerRowCol)*numPerRowCol+cor[1]//(size_of_board/numPerRowCol))


game_instance = Othello()
game_instance.mainloop()