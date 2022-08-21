from logging import exception
from tkinter import E
from turtle import left


a = [[0,2,2,2,2,2,2,2,1],
     [1,0,1,0,1,0,0,1,0],
     [2,0,1,0,0,2,0,0,0],
     [0,0,1,2,0,0,2,2,1],
     [0,0,0,2,2,1,0,1,0]
     ]


# length = len(board[0])
# height  = len(a)-1
def checkavi(board, row,col):
    length = len(board[0])
    height = len(board)-1
    blackAvi = False
    whiteAvi = False
    if(board[row][col] >0 and board[row][col] < 3):
        return 
    # for i in range(row+1,length):
    #   checking right ward
    # if(not (col >=length)):
    # try:
    if(col < length-1):
        # print("checking rightward")
        rightPivot = board[row][col+1]
        if (rightPivot>0 and rightPivot<3 ):
            for index in range(col+1,length):
                nextRight = board[row][index]
                if(nextRight>2 or nextRight<1):
                    break
                if(nextRight!= rightPivot):
                    if(rightPivot == 2):
                        whiteAvi = True
                        break
                    else:
                        blackAvi = True
                        break


    #   checking leftward
    # if(not(col <= 0)):
    if( col > 0 ):
        # print("checking leftward")

        leftPivot = board[row][col-1]
        if(leftPivot >0 and leftPivot<3):
            for index in range(col-1 ,0,-1):
                nextLeft = board[row][index]
                if(nextLeft>2 or nextLeft <1):
                    break

                if(nextLeft != leftPivot):
                    if(leftPivot == 2):
                        whiteAvi = True
                        break
                    else:
                        blackAvi = True
                        break

    #   checking downward
    if(not (whiteAvi and blackAvi) and row<height -1):
        # print("checking downward")

        # if(not row >= height):
        # print(row)
        # print(col)
        # print(height)
        # print(board[row][col])
        # if( row < height-1):
        downPivot = board[row+1][col]
        if(downPivot > 0 and downPivot <3):
            for index in range(row+1, height):
                nextDown = board[index][col]

                # print("in loop, index col is {}, next down is {}".format(index, nextDown))
                if(nextDown>2 or nextDown<1):
                    break
                if( nextDown != downPivot):
                    if(downPivot == 2):
                        whiteAvi = True
                        break
                    else:
                        blackAvi = True
                        break
    #   checking upward 
    if( not ( whiteAvi and blackAvi)  and row>0):
        # print("checking upward")

        # if(row > 0 ):
        upPivot = board[row-1][col]
        if(upPivot > 0 and upPivot < 3 ):
            for index in range(row-1,0,-1):
                nextUp  = board[index][col]
                if(nextUp>2 or nextUp <1):
                    break
                # print("index is {}, the up pivot is {}, and nextUp is {}".format(index, upPivot, nextUp))
                if(nextUp != upPivot ):

                    if(upPivot ==2):
                        whiteAvi = True
                        
                        break
                    else:
                        blackAvi = True
                        break
                        
    


        

    
    if(blackAvi):
            if(whiteAvi):
                return 5
            else:
                return  4
    elif(whiteAvi):
        return 3
    else:
        return 0



# print(checkavi(0,0))
# print(checkavi(4,2))
