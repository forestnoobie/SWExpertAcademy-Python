from copy import deepcopy

path = r'C:\Users\Nakyilkim\Desktop\LIFE\swexpert\input\sample_1767.txt'

board = []
with open(path) as f:
    lines = f.readlines()
    N = int(lines[1])
    for i in range(N):
        temp = list(map(int,lines[2+i].rstrip().split()))
        board.append(temp)

install = deepcopy(board)

## Direction
# 0 : No, 1: left , 2 : down , 3 : right, 4 : up
directions = [0,1,2,3,4]

def install(pos,direction):

    if direction == 0 :
        return

    elif direction == 1 :
        if sum(install[pos[0]][1:pos[1]]) != 0 :
            return False
        else :
            install[pos][1:pos[1]] = [2] * (pos[1] - 1)
            return True

    elif direction == 2:
        temp = []
        temp = [install[i][pos[1]] for i in range(pos[0],N)]
        if sum(temp) != 0 :
            return False
        else :
            for i in range(pos[0],N):
                install[i][pos[1]]  = 2
            return True

    elif direction == 3:
        if sum(install[pos[0]][pos[1]+1:N]) != 0 :
            return False
        else :
            install[pos][pos[1]+1:N] = [2] * (N - pos[1]-1)
            return True

    elif direction == 4:
        temp = []
        temp = [install[i][pos[1]] for i in range(pos[0],N)]

        if sum(temp) != 0 :
            return False
        else:
            for i in range(1,pos[0]):
                install[i][pos[1]] = 2
            return True
        


def search(now):


    return
