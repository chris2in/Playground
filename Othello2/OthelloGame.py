from tkinter import *

size_of_board =800
numPerRowCol = 8 
class Squre():
    def __init__(self,OthelloObject, x , y , outline = 'dark gray', indicator = 0 ):
        
        self.x = x
        self.y = y
        self.outline = outline
        self.indicator = indicator
        self.color = 'gray'
        length = size_of_board/numPerRowCol
        if(self.indicator ==1):
            self.color = 'black'
        elif(self.indicator ==2):
            self.color = 'white'
        else:
            self.color=  'gray'
    
        
        self.Rectangle = OthelloObject.canvas.create_rectangle(x*length,
                                                              y*length,
                                                              (x+1)*length,
                                                              (y+1)*length,
                                                              outline='dark gray')



    #   example of using this method in Othello:
    #           self.Squres[x][y].changeColor(self,3)
    #           where self will pass the Othello object here so you can access the canvas' functions to change color 
    def changeColor (self,OthelloObject,newIndi):
        color = 'gray'
        self.indicator=newIndi
        if(newIndi == 1):
            color = 'black'
        elif(newIndi ==2):
            color = 'white'
        elif(newIndi ==3):
            color = 'red'
        elif(newIndi ==4):
            color = 'blue'
        elif(newIndi ==5):
            color = 'light green'
        
        OthelloObject.canvas.itemconfig(self.Rectangle,fill = color)


    def changeIndi(self,newIndi):
        self.indicator=newIndi


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

        self.Squres[4][3].changeColor(self,1)
        self.Squres[3][4].changeColor(self,1)
        self.Squres[3][3].changeColor(self,2)
        self.Squres[4][4].changeColor(self,2)

        self.Squres[3][2].changeIndi(3)
        self.Squres[2][3].changeIndi(3)
        self.Squres[5][4].changeIndi(3)
        self.Squres[4][5].changeIndi(3)

        self.Squres[4][2].changeIndi(4)
        self.Squres[2][4].changeIndi(4)
        self.Squres[5][3].changeIndi(4)
        self.Squres[3][5].changeIndi(4)

        



    def click(self,event):
        result =  ([int(event.x//(size_of_board/numPerRowCol)), int(event.y//(size_of_board/numPerRowCol))])
        if(self.turn):
            if(self.Squres[result[0]][result[1]].indicator==3 or self.Squres[result[0]][result[1]].indicator==5):
                self.Squres[result[0]][result[1]].changeColor(self,1)

                self.turn = not   self.turn 
            else:
                print("wrong move, the indi is  ",self.Squres[result[0]][result[1]].indicator)
        else:
            if(self.Squres[result[0]][result[1]].indicator==4 or self.Squres[result[0]][result[1]].indicator==5):
                self.Squres[result[0]][result[1]].changeColor(self,2)
                self.turn = not   self.turn 

            else:
                print("wrong move, the indi is  ",self.Squres[result[0]][result[1]].indicator)

        
        
        print(result)

    def mainloop(self):
        self.window.mainloop()

game_instance= Othello()
game_instance.mainloop()