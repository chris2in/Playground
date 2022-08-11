a = [[0,1,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0]]


length = len(a[0])
def checkavi(row,col):
    blackAvi = False
    whiteAvi = False

    # for i in range(row+1,length):
    #   checking right ward


    if(blackAvi):
            if(whiteAvi):
                return 5
            else:
                return  3
    elif(whiteAvi):
        return 4
    else:
        return 0



checkavi(0,0)