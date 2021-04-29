Q =[-1] *4
board = []
domain = [0,1,2,3]
board = [domain]*4

N = len(board)

column = 0
row = 4
board[0] = 0
print(board)

i,j = row,column
for k in range(N):
    board1 = list(board)
    print(board1[k])
    if column in board1[k]:

        board1[k].remove(column)
        print(board1[k])


# for l in board1[k]:
#     if abs(j-l)== abs(k-i):
#         nboard =  list(board1[k])
#         board1[k].remove(l)
#         board1[k] = nboard
#
#
# if len(board1[k]==0):
#     print("No possible solutions")
