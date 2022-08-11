from unittest import result


file = open('test.txt','r')
Lines = file.readlines()
length = 4



def refresh(matrix,row,col):
    # for row in matrix:
    #     for index in row:
    blackAvi = False
    whiteAvi = False
    result = 0 
    #         #   piece by piece test later
    if(row == 0):
        if(col == 0):
            #   checking horiontally 
            if(matrix[0][1] > 0 and matrix[0][1]<3):
                print()
            if(matrix[1][0]>0 and matrix[1][0]<3):
            
                print()
        if(col == 3):
            print()
    
    # checkright
    pivot = matrix[row][col+index]
    if (not(pivot<1 or pivot > 2 )):

        for index in range(col+1, length):
            return 0 
            




    if(blackAvi):
        if(whiteAvi):
            return 5
        else:
            return  3
    elif(whiteAvi):
        return 4
    else:
        return 0
            

    




    return result


for i in Lines:
    matrix = []
    updatedMatrix=[]
    period  = i.split('.')
    for o in period:
        row = []
        for p in o.split(','):
            row.append(int(p))
        matrix.append(row)
        # updatedMatrix.append(row)
    
    matrix = refresh(matrix)
    for row in range(len(matrix)):
        updatedMatrix.append([])
        for col in range(len(row)):
            updatedMatrix[row].append(refresh(matrix,row,col))
        
            