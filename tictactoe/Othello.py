from tkinter import *
import numpy as np

size_of_board= 1600


class Othello():

    def __init__(self):
        self.window = Tk()
        # self.window.attributes('-fullscreen',True)
        self.window.title("Try Othelowsomehting")

        self.canvas = Canvas(self.window, width= size_of_board,height=size_of_board)
        self.canvas.pack()

        self.window.bind('<Button-1>',self.click)
        
    # change  s
    def click(self, event):
        grid_position = [event.x,event.y]
        position = self.covertToPosition(grid_position)

    def convertToposition(self, grid_position):
        grid_position = np.array(grid_position)
        return np.array(grid_position // (size_of_board/3),dtype = int)