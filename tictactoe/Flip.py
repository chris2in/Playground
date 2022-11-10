


a= [
    [0,2,2,1,2],
    [0,0,1,1,2],
    [0,0,0,1,2],
    [0,0,0,0,0],
    [0,0,0,0,0]
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
    
    # endWell =False
    if( col < widthMAX -1 ) :
        
        
        #   list to traverse
        traverseList = board[row][col+1:]
        directionFlip = 0 
        # print("start checkign right ")
        for i in traverseList:
            if( i> 0 and i < 3 and i != piece):
                # print("one pass, next one")
                directionFlip +=1
                
            else:
                # print("stopped")
                if(i == piece):
                    # print("we get to flip some")
                    for index in range(directionFlip):
                        board[row][col+index+1] = piece
                    score += directionFlip
                
    if( col > 1):
        traverseList = board[row][0:col]
        traverseList.reverse()
        directionFlip = 0
        # print("reverse list is {}".format(traverseList))
        for i in traverseList:
            if( i > 0 and i < 3 and i != piece):
                directionFlip +=1
            else:
                if( i == piece):
                    for index in range(directionFlip):
                        board[row][col-index-1] = piece
                    score  += directionFlip

    if(row > 1 ):
        traverseList = []
        for i in range(row-1,-1,-1):
            traverseList.append(board[i][col])
        for i in traverseList:
            if( i > 0 and i < 3 and i != piece):
                directionFlip +=1
            else:
                if( i == piece):
                    for index in range(directionFlip):
                        board[row+index+1][col] = piece
                    score  += directionFlip
    
    if( row < heightMAX -1):
        traverseList = []
        for i in range(0,row):
            traverseList.append(board[i][col])
        for i in traverseList:
            if( i > 0 and i < 3 and i != piece):
                directionFlip +=1
            else:
                if( i == piece):
                    for index in range(directionFlip):
                        board[row-index-1][col] = piece
                    score  += directionFlip


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


flip(a,0,0,1)
flip(a,1,1,1)
flip(a,2,3,2)

for i in range(len(a)):
    for o in range(i):
        print(a[i][o],end="\t")
    print()





