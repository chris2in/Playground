# subject = [0,1,1,1,2,0]
# subject = [0,1,1,1,2,0]
# subject = [0,1,1,1,2,1,0]
# subject = [0,1,1,1,2,2,0]
# subject = [0,1,1,1,1,0]
# subject = [0,1,1,1,0]
subject = [0,1,2]


def testing(array,indi):
    # print(array[indi])
    newBase = indi+1
    # print(newBase)
    result = 0 
    base = array[newBase]
    # print(base)
    if(base ==1 or base ==2 ):
        print("get here")
        print(newBase-1)
        for i in range(newBase,len(indi)):
            print('comparing {} and {}'.format(array[i],base))
            if(array[i]!=base):
                if(array[i]!= 1 and array[i]!=2 ):
                    print("end of list")
                    break 
                elif(array[i]==2):
                    return('2')
                elif(array[i]==1):
                    return ('1')

            

    return result 

# if(testing(subject,0) != 2):
#     print('fail')
print(testing(subject,len(subject)-1))