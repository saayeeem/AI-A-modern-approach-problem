import math

# puzzle = [[6,1,10,2],[7,11,4,14],[5,10000,9,15],[8,12,13,3]]
# puzzle = [[7,1,2],[5,10000,4],[8,3,6]]
puzzle = [[13,10,11,6],[5,7,4,8],[1,12,14,9],[3,15,2,10000]]

# puzzle = [[10000, 1, 3],[4, 2, 5],[7, 8, 6]]
# puzzle = [[1, 2, 3],[10000, 4, 6],[7, 5, 8]]
# puzzle = [[1, 8, 2],[10000, 4, 3],[7, 6, 5]] #last three puzzle i took from internet to test the efficiency of program
list = []
def returnInversion(puzzle):
    count = 0
    rcount = 0

    for row in puzzle:
        x = len(row)
        for col in row:
            list.append(col)
            dimensions = len(list)


    blanktilePostion = list.index(10000)
    for i in range(len(list)):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1] :
                list[j], list[j+1] = list[j+1], list[j]
                count = count +1
    for k in range(len(list)):
        nindex = list.index(10000)
    inversions = count - (nindex-blanktilePostion)
    blanktilePostionRow = math.ceil((dimensions-blanktilePostion)/x)
    print("Puzzle: ",puzzle)
    print("Inversion:",inversions)
    print("Dimensions:",dimensions)
    print("Blank tile Row Postion From Bottom:",blanktilePostionRow)

    return inversions,blanktilePostionRow,dimensions
def isEven(number):
    if(number%2==0): return True
    else: return False
def solvablity(inversions,blanktilePostion,dimensions):
    if(isEven(dimensions)==False and isEven(inversions)==True):
        print("Solvable")
    elif(isEven(dimensions)==True and isEven(blanktilePostionRow)==False and isEven(inversions)==True):
        print("Solvable")
    elif(isEven(dimensions)==True and isEven(blanktilePostionRow)==True and isEven(inversions)==False):
        print("Solvable")
    else:
        print("Not Solvable")
    return solvablity

inversions,blanktilePostionRow,dimensions = returnInversion(puzzle)
solvablity(inversions,blanktilePostionRow,dimensions)
