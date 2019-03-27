# N = 5
# K = 1
# board = [[0 for i in range(N)] for j in range(N)]
#
# board[0] = [ int(x) for x in '9 3 2 3 2'.split(' ')]
# board[1] = [ int(x) for x in '6 3 1 7 5'.split(' ')]
# board[2] = [ int(x) for x in '3 4 8 9 9'.split(' ')]
# board[3] = [ int(x) for x in '2 3 7 7 7'.split(' ')]
#board[4] = [ int(x) for x in '7 6 5 5 8'.split(' ')]

N = 3
K =2

board = []
board.append([1,2,1])
board.append([2,1,2])
board.append([1,2 ,1])

# 1. 가장 높은 봉우리 선택
# 1.1 주위 탐색
# 2. 깍을지 말지 결정 - > 깎는다면 어디를 ? . 자기 보다 같거나 높은거
# 2.1 깎을 곳 선택 후 얼마나 깍을 지도 정하기
# 3. 다음 step 이동 위 반 복

# 상하좌우
dx = [0 , 0 , -1 , 1]
dy = [-1, 1 , 0 , 0]


max = 0
max_list = []

for i in range(N):
    for j in range(N):

        v = board[i][j]
        if v > max:
            max = v
            max_list = [[i,j]]
        elif v == max:
            max_list.append([i,j])


# class search(self):
#     def __init__(self, start):
#         self.start = start
#         self.board = board
#
#     def move(self):
max_path = []

def search(start=[0,0], path=[[0,0]], dig = 1):

    ## Base Case
    # 더 이상 움직을 곳이 없을 때
    # 주변이 모두 자기 자신보다 클 때
    global  total_path, max_path
    anwser =[]
    move = 0

    st_v = board[start[0]][start[1]]
    for idx in range(4):
        ny = start[0] + dy[idx]
        nx = start[1] + dx[idx]

        if ny < 0 or ny > N -1 or nx < 0 or nx > N -1:
            continue
        nv =  board[ny][nx]
        print("st_v:{} nv:{}".format(st_v,nv))

        if nv < st_v:
            move = 1
            path.append([ny,nx])
            anwser = search([ny,nx],path,dig)
            path.pop()

        elif nv - st_v < K and nv - st_v >= 0:

            if dig ==1 :
                differ = nv-st_v
                for i in range(differ+1, K+1):

                    print("Dig",ny,nx,i)
                    board[ny][nx] -= i

                    path.append(([ny,nx]))
                    move = 1
                    anwser = search([ny,nx],path, dig=0)
                    path.pop()
                    board[ny][nx] += i

        elif nv -st_v >= K:
            continue

    ## Base Case
    if move == 0 :
        print("Path Print",path)

        print("Path length {} max path length {}".format(len(path),len(max_path)))

        if len(path) > len(max_path):
            print("Changing Max_path",path)
            max_path =  [x for x in path]
        return

for start in max_list:
    search(start=start,path=[start])
    print(max_path)