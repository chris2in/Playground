a= [
    [0,1,2,1,2],
    [0,0,0,0,0],
    [0,1,2,1,2],
    [0,2,1,1,2],
    [0,1,1,2,1]
]

b = [
    [0,1,1,1,2],
    [2,1,0,2,1],
    [1,2,2,2,0],
    [0,1,1,1,0],
    [2,1,2,1,1]


]


def flip(board,row,col,piece):
    #takes in the 2d array board, x, and y
    #   returns the udpated board 

    score = 0
    # board [0][0] = 20
    widthMAX  = len(board[0])
    heightMAX = len(board)-1

    anchor = piece
    
    #   checking rightward
    if(col < widthMAX-1):
        # nextRight = board[row][col]
        rightPivot = board[row][col+1]
        if(rightPivot > 0 and rightPivot < 3 ):
            for index in range(col+1,widthMAX):
                nextRight = board[row][index]
                if(nextRight > 2 or nextRight < 1):
                    break
                if(nextRight != rightPivot):
                    # if()
                    #   continue here





    return score 

flip(b,1,2,2)





# for i in range(len(a[1])):
#     print( flip(a,1,i))

for i in b:
    for o in i:
        print(o, end = ' ')
    print()