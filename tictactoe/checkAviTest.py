a = [[0,2,2,2,2,2,2,2,1],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0]]


length = len(a[0])
def checkavi(row,col):
    blackAvi = False
    whiteAvi = False

    # for i in range(row+1,length):
    #   checking right ward
    rightPivot = a[row][col+1]
    if (rightPivot>0 and rightPivot<3 ):
        for index in range(col+1,length):
            nextRight = a[row][index]
            if(nextRight>2 or nextRight<1):
                break
            if(nextRight!= rightPivot):
                if(rightPivot == 2):
                    blackAvi = True
                else:
                    whiteAvi = True


    if(blackAvi):
            if(whiteAvi):
                return 5
            else:
                return  3
    elif(whiteAvi):
        return 4
    else:
        return 0



print(checkavi(0,0))