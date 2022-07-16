from tkinter import *
import numpy as np

size_of_board= 800
numPerRowCol = 8


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



    # # change  s
    # def click(self, event):
    #     grid_position = [event.x,event.y]
    #     position = self.covertToPosition(grid_position)

    # def convertToposition(self, grid_position):
    #     grid_position = np.array(grid_position)
    #     return np.array(grid_position // (size_of_board/3),dtype = int)

    def click(self,event):
        print("x:",event.x)
        print("y:",event.y)
        print(event.x // (size_of_board//numPerRowCol)+1)


    def initialize_board(self):
        for i in range(numPerRowCol-1):
            self.canvas.create_line((i + 1) * size_of_board / numPerRowCol-1, 0, (i + 1) * size_of_board / numPerRowCol-1, size_of_board)

        for i in range(numPerRowCol-1):
            self.canvas.create_line(0, (i + 1) * size_of_board / numPerRowCol-1, size_of_board, (i + 1) * size_of_board / numPerRowCol-1)

    def mainloop(self):
        self.window.mainloop()


game = Othello()
game.mainloop()