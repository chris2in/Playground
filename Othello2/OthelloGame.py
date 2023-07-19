from tkinter import *

size_of_board =800
numPerRowCol = 8 
class Squre():
    def __init__(self,OthelloObject, x , y , outline = 'dark gray', indicator = 0 ):
        
        self.x = x
        self.y = y
        self.outline = outline
        self.indicator = indicator

class Othello():
    def __init__(self):

        #   true for black s turn and false for white s turn 
        self.turn = True

        self.window = Tk()

        self.window.title("Othello again")

        self.canvas = Canvas(self.window, width = size_of_board, height= size_of_board, bg = 'lightgray')
        self.canvas.pack()

        self.window.bind('<Button-1>', self.click)

        self.Squres= []
        for i in range(numPerRowCol):
            self.Squres.append([])
            for o in range(numPerRowCol):
                self.Squres[i].append(Squre(self,i,o))





    def click(self,event):
        return ([int(event.x//(size_of_board/numPerRowCol)), int(event.y//(size_of_board/numPerRowCol))])
    
    def mainloop(self):
        self.window.mainloop()

game_instance= Othello()
game_instance.mainloop()