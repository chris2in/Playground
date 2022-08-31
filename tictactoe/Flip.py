from distutils.debug import DEBUG


a= [
    [0,1,2,1,2],
    [0,0,0,0,0],
    [0,1,2,1,2],
    [0,2,1,1,2],
    [0,1,1,2,1]
]

b = [
    [0,1,1,1,2],
    [1,1,0,2,1],
    [1,0,1,1,1],
    [0,1,2,1,0],
    [2,0,1,1,1]


]
DEBUGTEST = True

def flip(board,row,col,piece):
    #takes in the 2d array board, x, and y
    #   returns the udpated board 

    score = 0
    # board [0][0] = 20
    widthMAX  = len(board[0])
    heightMAX = len(board)-1

    # anchor = piece
    board[row][col]= piece
    

    if( col < widthMAX -1 ) :
        nextRight = board[row][col+1]
        for index in range(col, widthMAX):
            print(board[row][index])
    '''
    #   checking rightward
    if(col < widthMAX-1):
        # nextRight = board[row][col]
        # pivot = board[ row][col]
        # print(pivot)\
        directionScore = 0
        nextRight = board[row][col+1]
        if(nextRight>0 and nextRight<3 and nextRight != piece):
            for index in range(col+1,widthMAX):
                if(board[row][index] == piece):
                    print("found it, break")
                    break
                else:
                    directionScore +=1
            for index in range(1,directionScore+1):
                board[row][col+index] = piece
                print("FLIP")
        score += directionScore
        if(DEBUGTEST):
            print("right has {} flip".format(directionScore))

    #   checking leftward
    if(col >= 0):
        nextLeft = board[row][col-1]
        directionScore = 0
        if(nextLeft>0 and nextLeft < 3 and nextLeft != piece):
            for index in range(col-1,0,-1):
                if(board[row][index] == piece):
                    break
                else:
                    directionScore +=1 
            for index in range(1, directionScore+1 ):
                board[row][col-index] = piece
        score += directionScore
        if(DEBUGTEST):
            print("left has {} flip".format(directionScore))
    
    #   checking downward
    if(row < heightMAX):
        nextDown = board[row+1][col ]
        directionScore = 0 
        if(nextDown>0 and nextDown < 3 and nextDown != piece):
            for index in range(row +1 , heightMAX):
                if(board[index][col] ==piece):
                    break
                else:
                    directionScore+=1
            for index in range(1, directionScore+1):
                board[row+index][col] = piece
        score += directionScore
    
        if(DEBUGTEST):
            print("down has {} flip".format(directionScore))

    #   checking upward
    if(row>= 0 ):
        nextUp = board[ row-1][col]
        directionScore = 0 
        if( nextUp > 0 and nextUp <3 and nextUp != piece):
            for index in range(row -1, 0 , -1):
                if(board[index][col] == piece):
                    break
                else:
                    print("the row {} and col {} is {}".format(index,col,board[index][col]))
                    directionScore +=1
                
                
            for index in range(1, directionScore+1):
                board[row-index][col] = piece
        score += directionScore 

        if(True):
            print("up has {} flip".format(directionScore))
       '''     

    print(score)




    return score 

flip(b,2,1,2)





# for i in range(len(a[1])):
#     print( flip(a,1,i))

for i in b:
    for o in i:
        print(o, end = ' ')
    print()