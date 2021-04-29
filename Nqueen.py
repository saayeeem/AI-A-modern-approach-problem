Q=[-1] *4
n = len(Q)
r = 0
def placeQueen(Q,r):
    if r == n :
        print(Q)
    else:
        for j in range(n):
            legal = True
            for i in range(r):
                if((Q[i]==j) or (Q[i]==j+r-i) or (Q[i]==j-r+i)):
                    legal = False

            if legal:
                Q[r]=j
                placeQueen(Q,r+1)

placeQueen(Q,r)
