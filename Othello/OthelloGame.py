from tkinter import *


size_of_board = 800
numperRowCol = 8 

class Othello():

    def __init__(self):
        self.window= Tk()

        self.window.title("Othello")

        self.canvas = Canvas(self.windwo, width = size_of_board, height= size_of_board, bg = 'lightgray')
        self.canvas.pack()

        self.window.bind('<Button-1>',self.click)

        self.Square= []


    def convertGridToBoard(self):
        return 

    def click(self,event):

        boardPosition = self.convertGridToBoard()
