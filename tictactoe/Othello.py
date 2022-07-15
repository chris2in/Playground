from tkinter import *

size_of_board= 1600


class Othello():

    def __init__(self):
        self.window = Tk()
        # self.window.attributes('-fullscreen',True)
        self.window.title("Try Othelowsomehting")

        self.canvas = Canvas(self.window, width= size_of_board,height=size_of_board)
        self.canvas.pack()

        self.window.bind('<Button-1>',self.click)
        
    # change 