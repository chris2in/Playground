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

        self.firstSquare = self.canvas.create_rectangle(0,0,300,300)
        # t = Timer(4000,self.changeColor(self.firstSquare))
        # t.start()
        


        # self.initialize_board()

    
    # def inializ
    def mainloop(self):
        self.window.mainloop()

    def changeColor(self,shape):
        
        self.canvas.itemconfig(shape,fill='green')
        # print()

    def click(self, event):
        self.changeColor(self.firstSquare)
        return 

game_instance = Othello()
game_instance.mainloop()