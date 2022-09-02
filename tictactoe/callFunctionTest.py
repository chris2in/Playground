import Flip


b = [
    [0,1,1,1,2],
    [2,1,0,2,1],
    [1,2,2,2,0],
    [0,1,1,1,0],
    [2,1,2,1,1]
]

Flip.flip(b,0,0,2)



for i in b:
    for o in i:
        print(o, end = ' ')
    print()